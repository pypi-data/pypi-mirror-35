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
from sonicprobe import helpers
from pyinotify import IN_DELETE


DEFAULT_TIMEOUT = 90
LOG             = logging.getLogger('sosbackups.classes.rsync')
_DATE_FORMAT    = '%Y-%m-%d %H:%M:%S'


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
        self._notifiers        = None
        self.notifications     = bool(self.config['inotify'].get('notifications', True))

        if 'rsync' in self.config['inotify']:
            self.rsync_max_retries = int(self.config['inotify']['rsync'].get('max_retries') or 0)
            self.rsync_path        = self.config['inotify']['rsync'].get('bin_path') or 'rsync'
            self.remote_rsync_path = self.config['inotify']['rsync'].get('remote_bin_path') or 'rsync'
            self.rsync_args        = self.config['inotify']['rsync'].get('args')

        if self.config['general'].get('notifiers_path'):
            self._notifiers = DWhoPushNotifications(self.server_id,
                                                    self.config['general']['notifiers_path'])

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

        if 'notifications' in params:
            self.notifications = bool(params['notifications'])

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

        while True:
            x = p.stdout.readline()
            if x == '' and p.poll() is not None:
                break
            x = x.rstrip()
            if x:
                LOG.info(x.rstrip())
        if p.returncode:
            raise subprocess.CalledProcessError(p.returncode, opts['args'][0])

        return p

    def _process_failed(self, filepath, process, opts, nb_retries, error):
        errors = {'stderr': None,
                  'error':  error}

        if process.returncode == 23:
            if not os.path.exists(filepath):
                LOG.warning("file deleted before synchronization. (path: %r)", filepath)
                return False
        elif process.returncode == 24:
            LOG.debug("vanished source file. (path: %r)", filepath)
            if nb_retries < opts['max_retries']:
                nb_retries += 1
                LOG.warning("retrying %s/%s caused by vanished source file.", nb_retries, opts['max_retries'])
                return

        if process:
            errors['stderr'] = process.stderr.read()
            LOG.error(errors['stderr'])

        if nb_retries < opts['max_retries']:
            nb_retries += 1
            LOG.warning("retrying %s/%s.", nb_retries, opts['max_retries'])
        else:
            LOG.exception(repr(error))
            return errors

    def exec_rsync(self, params, event, filepath, notify = False):
        if self.last_gc + DEFAULT_TIMEOUT >= time.time():
            gc.collect()
            self.last_gc = time.time()

        if event.dir:
            filepath += os.path.sep

        (process, errors) = (None, None)

        if getattr(event, 'sync', None) is False:
            return

        opts              = self._get_rsync_params(params, event, filepath)
        nb_retries        = 0

        if not opts:
            return

        while True:
            try:
                errors  = None
                process = self._run_process(opts)

                if process.returncode:
                    raise subprocess.CalledProcessError(p.returncode, opts['args'][0])
                break
            except Exception, e:
                errors = self._process_failed(filepath, process, nb_retries, opts, e)
                if errors or errors is False:
                    break

        if notify:
            self.send_notifications(filepath, event, errors)

        return errors

    def try_exec_rsync(self, params, event, filepath, notify = True):
        errors = None

        try:
            errors = self.exec_rsync(params, event, filepath)
        except Exception, e:
            errors = e
            LOG.exception(repr(e))

        if notify:
            self.send_notifications(filepath, event, errors)

        return errors

    def send_notifications(self, filepath, event, errors = None):
        if not self.notifications:
            return

        state = {'errors':    [],
                 'filepath':  filepath,
                 'logged_at': time.strftime(_DATE_FORMAT)}

        if not errors:
            state['status'] = 'success'
        else:
            state['status'] = 'failure'
            state['errors'].append({'error':  repr(errors['error']),
                                    'stderr': errors['stderr']})

        if not getattr(event, 'caller_id', None):
            return self._notifiers(state)

        caller_state = DWHO_SHARED.get('sosbackups', event.caller_id)
        if not caller_state:
            return self._notifiers(state)

        if 'errors' not in caller_state:
            caller_state['errors'] = []

        if errors:
            caller_state['errors'].append(state['errors'][0])

        if 'stats' not in caller_state:
            caller_state['stats'] = {'files':   {'success': 0,
                                                 'failure': 0,
                                                 'size':    0,
                                                 'total':   0},
                                     'dirs':    {'success': 0,
                                                 'failure': 0,
                                                 'total':   0},
                                     'total':    0,
                                     'duration': -1}

        if event.dir:
            key = 'dirs'
        else:
            key = 'files'

        if getattr(event, 'sync', None) is not False:
            if errors:
                caller_state['stats'][key]['failure'] += 1
            else:
                caller_state['stats'][key]['success'] += 1

                if key == 'files' and os.path.exists(filepath):
                    caller_state['stats'][key]['size'] += os.path.getsize(filepath)

            caller_state['stats'][key]['total'] += 1
            caller_state['stats']['total'] += 1

        if hasattr(event, 'last_file') and event.last_file != filepath:
            return

        if caller_state['errors']:
            caller_state['status'] = 'failure'
        else:
            caller_state['status'] = 'success'

        caller_state['ended_at'] = time.strftime(_DATE_FORMAT)

        if caller_state.get('started_at') and caller_state.get('ended_at'):
            started = datetime.datetime.strptime(caller_state['started_at'], _DATE_FORMAT)
            caller_state['stats']['duration'] = (datetime.datetime.now() - started).total_seconds()

        state = caller_state.copy()

        DWHO_SHARED.remove('sosbackups', event.caller_id)

        return self._notifiers(state)
