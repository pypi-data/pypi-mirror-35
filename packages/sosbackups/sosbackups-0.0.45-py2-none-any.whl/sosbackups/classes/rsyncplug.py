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
import datetime
import gc
import logging
import os
import shellescape
import shutil
import subprocess
import time

from dwho.classes.inoplugs import DWhoInoEventPlugBase
from dwho.classes.notifiers import DWhoPushNotifications
from dwho.config import DWHO_SHARED
from sosbackups.plugins.cronsync import DATE_FORMAT, DEFAULT_STATS
from sonicprobe import helpers
from pyinotify import IN_DELETE


DEFAULT_TIMEOUT = 90
LOG             = logging.getLogger('sosbackups.classes.rsync')


class SosBackupsRsyncPlug(DWhoInoEventPlugBase):
    __metaclass__ = abc.ABCMeta

    def init(self, config):
        DWhoInoEventPlugBase.init(self, config)

        self.last_gc           = time.time()

        self.cfg_path          = None
        self.event             = None
        self.filepath          = None

        self.nb_retries        = 0
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

    def get_event_params(self):
        if hasattr(self.event, 'plugins') \
           and isinstance(self.event.plugins, dict) \
           and self.PLUGIN_NAME in self.event.plugins:
            return self.event.plugins[self.PLUGIN_NAME].copy()

        return {}

    def _get_rsync_params(self, params, filepath):
        bin_path        = self.rsync_path
        remote_bin_path = self.remote_rsync_path
        args            = list(self.rsync_args)
        max_retries     = self.rsync_max_retries
        to_delete       = (self.event.mask & IN_DELETE) != 0

        if params.get('dest'):
            dest = params['dest']
        else:
            if 'prefix_path' in params:
                prefix_path = params['prefix_path']
            else:
                prefix_path = self.prefix_path

            dest = self.realdstpath(self.event, filepath, prefix_path)

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

                if self.event.dir:
                    dest     = os.path.dirname(destdir)
                    filepath = os.path.dirname(filepath.rstrip(os.path.sep)) + os.path.sep
                else:
                    filepath = os.path.dirname(filepath) + os.path.sep

            destparam = "%s:%s" % (params['host'], dest)
        else:
            destparam = dest

            if to_delete:
                if os.path.exists(dest):
                    if self.event.dir:
                        shutil.rmtree(dest, True)
                    elif not os.path.isdir(dest):
                        os.unlink(dest)
                return

            if not os.path.exists(filepath):
                return

            if not os.path.isdir(destdir):
                helpers.make_dirs(destdir)

        return {'max_retries': max_retries,
                'args':        [bin_path] + args + ['-s', filepath, destparam]}

    def _run_process(self, opts):
        LOG.debug("rsync cmd: %r", " ".join(opts['args']))
        p = subprocess.Popen(opts['args'],
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)

        (stdout, stderr) = p.communicate()

        if stdout:
            for x in stdout.splitlines():
                if x:
                    LOG.info(x)

        return (p.returncode, stderr)

    def _process_failed(self, filepath, returncode, stderr, opts, error):
        errors = {'stderr': stderr,
                  'error':  error}

        if returncode == 23:
            if not os.path.exists(filepath):
                LOG.warning("file deleted before synchronization. (path: %r)", filepath)
                return False
        elif returncode == 24:
            LOG.debug("vanished source file. (path: %r)", filepath)
            if self.nb_retries < opts['max_retries']:
                self.nb_retries += 1
                LOG.warning("retrying %s/%s caused by vanished source file.", self.nb_retries, opts['max_retries'])
                return

        if errors['stderr']:
            for x in errors['stderr'].splitlines():
                LOG.error(x)

        if self.nb_retries < opts['max_retries']:
            self.nb_retries += 1
            LOG.warning("retrying %s/%s.", self.nb_retries, opts['max_retries'])
        else:
            LOG.exception(repr(error))
            return errors

    def exec_rsync(self, params, filepath, set_state = False):
        if self.last_gc + DEFAULT_TIMEOUT >= time.time():
            gc.collect()
            self.last_gc = time.time()

        if self.event.dir:
            filepath += os.path.sep

        errors          = None
        opts            = self._get_rsync_params(params, filepath)
        self.nb_retries = 0

        if not opts:
            return

        while True:
            try:
                errors               = None
                (returncode, stderr) = self._run_process(opts)
                if returncode:
                    raise subprocess.CalledProcessError(returncode, opts['args'][0])
                break
            except Exception, e:
                errors = self._process_failed(filepath, returncode, stderr, opts, e)
                if errors or errors is False:
                    break

        if set_state:
            self._set_state(filepath, errors)

        return errors

    def try_exec_rsync(self, params, filepath, set_state = True):
        errors = None

        try:
            errors = self.exec_rsync(params, filepath, False)
        except Exception, e:
            errors = e
            LOG.exception(repr(e))

        if set_state:
            self._set_state(filepath, errors)

        return errors

    def _set_state(self, filepath, errors = None):
        if self.event.dir:
            key      = 'dirs'
            filetype = 'directory'
        else:
            key      = 'files'
            filetype = 'file'

        state = {'errors':    [],
                 'filepath':  filepath,
                 'filetype':  filetype,
                 'logged_at': time.strftime(DATE_FORMAT),
                 'stats':     DEFAULT_STATS.copy()}

        if not errors:
            state['status'] = 'success'
            state['stats'][key]['success'] += 1
            state['stats']['total']['success'] += 1
        else:
            state['status'] = 'failure'
            state['stats'][key]['failure'] += 1
            state['stats']['total']['failure'] += 1
            state['errors'].append({'error':  repr(errors['error']),
                                    'stderr': errors['stderr']})

        state['stats'][key]['total'] += 1
        state['stats']['total']['total'] += 1

        self.event.state[self.PLUGIN_NAME] = state

    def __call__(self, cfg_path, event, filepath):
        self.cfg_path = cfg_path
        self.event    = event
        self.filepath = filepath

        try:
            self.run()
        finally:
            if hasattr(self.event, 'tevent'):
                self.event.tevent.set()
