# -*- coding: utf-8 -*-
"""rsync plugin"""

__author__  = "Adrien DELLE CAVE <adc@doowan.net>"
__license__ = """
    Copyright (C) 2018  doowan

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA..
"""

import abc
import gc
import logging
import os
import shellescape
import shutil
import subprocess
import time

from dwho.classes.inoplugs import DWhoInoEventPlugBase
from sonicprobe import helpers
from pyinotify import IN_DELETE


DEFAULT_TIMEOUT = 90
LOG             = logging.getLogger('sosbackups.classes.rsync')


class SosBackupsRsyncPlug(DWhoInoEventPlugBase):
    __metaclass__ = abc.ABCMeta

    def init(self, config):
        DWhoInoEventPlugBase.init(self, config)

        self.last_gc           = time.time()

        self.rsync_max_retries = 0
        self.rsync_path        = 'rsync'
        self.remote_rsync_path = 'rsync'
        self.rsync_args        = []
        self.prefix_path       = self.config['inotify'].get('prefix_path')

        if 'rsync' in self.config['inotify']:
            self.rsync_max_retries = int(self.config['inotify']['rsync'].get('max_retries') or 0)
            self.rsync_path        = self.config['inotify']['rsync'].get('bin_path') or 'rsync'
            self.remote_rsync_path = self.config['inotify']['rsync'].get('remote_bin_path') or 'rsync'
            self.rsync_args        = self.config['inotify']['rsync'].get('args')

    def _get_rsync_params(self, params, event, filepath):
        bin_path        = self.rsync_path
        remote_bin_path = self.remote_rsync_path
        args            = list(self.rsync_args)
        max_retries     = self.rsync_max_retries
        to_delete       = (event.mask & IN_DELETE) != 0

        if params.get('dest'):
            dest = params['dest']
        else:
            if 'prefix_path' in params:
                prefix_path = params['prefix_path']
            else:
                prefix_path = self.prefix_path

            dest = self.realdstpath(event, filepath, prefix_path)

        if 'rsync' in params:
            if params['rsync'].get('bin_path'):
                bin_path = params['rsync']['bin_path']

            if params['rsync'].get('remote_bin_path'):
                remote_bin_path = params['rsync']['remote_bin_path']

            if 'args' in params['rsync']:
                args += params['rsync']['args']

            if 'max_retries' in params['rsync']:
                max_retries = int(params['rsync']['max_retries'])

        destdir   = os.path.dirname(dest)

        if params.get('host'):
            if not to_delete:
                args += ['--rsync-path', "mkdir -p %s && %s"
                         % (shellescape.quote(destdir),
                            shellescape.quote(remote_bin_path))]
            else:
                dest  = destdir
                args += ['--delete-after',
                         '--existing',
                         '--ignore-existing',
                         '--rsync-path',
                         remote_bin_path]

                if event.dir:
                    dest     = os.path.dirname(destdir)
                    filepath = os.path.dirname(filepath.rstrip(os.path.sep)) + os.path.sep
                else:
                    filepath = os.path.dirname(filepath) + os.path.sep

            destparam = "%s:%s" % (params['host'], dest)
        else:
            destparam = dest

            if to_delete:
                if os.path.exists(dest):
                    if event.dir:
                        shutil.rmtree(dest, True)
                    else:
                        os.unlink(dest)
                return

            if not os.path.isdir(destdir):
                helpers.make_dirs(destdir)

        return {'max_retries': max_retries,
                'args':        [bin_path] + args + ['-s', filepath, destparam]}

    def run_rsync_cmd(self, params, event, filepath):
        if self.last_gc + DEFAULT_TIMEOUT >= time.time():
            gc.collect()
            self.last_gc = time.time()

        if event.dir:
            filepath += os.path.sep

        p          = None
        opts       = self._get_rsync_params(params, event, filepath)
        nb_retries = 0

        if not opts:
            return

        while True:
            try:
                LOG.debug("rsync cmd: %r", " ".join(opts['args']))
                p = subprocess.Popen(opts['args'],
                                     stdout = subprocess.PIPE,
                                     stderr = subprocess.PIPE)

                while True:
                    x = p.stdout.readline()
                    if x == '' and p.poll() is not None:
                        break
                    LOG.info(x.rstrip())
                if p.returncode:
                    raise subprocess.CalledProcessError(p.returncode, opts['args'][0])
                break
            except Exception, e:
                if p:
                    LOG.error(p.stderr.read())

                if nb_retries < opts['max_retries']:
                    nb_retries += 1
                    LOG.warning("retrying %s/%s", nb_retries, opts['max_retries'])
                else:
                    LOG.exception(repr(e))
                    break
