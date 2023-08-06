# -*- coding: utf-8 -*-
"""cronsync plugin"""

__author__  = "Adrien DELLE CAVE"
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


import datetime
import logging
import os
import pyinotify
import re
import threading
import time

from croniter import croniter
from dwho.classes.errors import DWhoConfigurationError
from dwho.classes.inotify import DWhoInotifyEventHandler
from dwho.classes.plugins import DWhoPluginBase, PLUGINS
from dwho.config import DWHO_SHARED
from sonicprobe import helpers
from sonicprobe.libs import workerpool


LOG              = logging.getLogger('sosbackups.plugins.cronsync')
WORKER_LIFETIME  = 300
_DATE_FORMAT     = '%Y-%m-%d %H:%M:%S'
_KILLED          = False


class SosBackupsScanEven(object):
    def __init__(self, pathname, caller, caller_id, plugins = None, sync = True):
        self.pathname  = pathname
        self.dir       = os.path.isdir(pathname)
        self.mask      = 0
        self.maskname  = 'SB_IN_SCAN'
        self.caller    = caller
        self.caller_id = caller_id
        self.sync      = bool(sync)
        self.plugins   = plugins
        self.finished  = False


class SosBackupsScanFinishEven(SosBackupsScanEven):
    def __init__(self, pathname, caller, caller_id, plugins = None, sync = False):
        SosBackupsScanEven.__init__(self, pathname, caller, caller_id, plugins, sync)
        self.finished  = True


class SosBackupsCronScan(threading.Thread):
    def __init__(self, name, xpath, options = None):
        threading.Thread.__init__(self)

        self.caller             = 'cronsync'
        self.caller_id          = "%s:%s" % (name,
                                             time.strftime(_DATE_FORMAT))
        self.name               = name
        self.xpath              = xpath
        self.inotify            = DWHO_SHARED.get('sosbackups', 'inotify')
        self.handler            = DWhoInotifyEventHandler(dw_inotify = self.inotify)
        self.options            = options
        self.options['format']  = options.get('format') or False
        self.exclude_patterns   = set()
        self.include_plugins    = []
        self.plugins            = {}
        self.started_at         = None

        if 'plugins' in options:
            plugins = options.pop('plugins')
            if isinstance(plugins, basestring):
                self.include_plugins = [plugins]
            elif isinstance(plugins, list):
                self.include_plugins = plugins
            elif isinstance(plugins, dict):
                for plug_name, plug_opts in plugins.iteritems():
                    self.include_plugins.append(plug_name)
                    self.plugins[plug_name] = plug_opts

        if 'exclude_files' in options:
            exclude_files = options.pop('exclude_files')

            if isinstance(exclude_files, basestring):
                exclude_files = [exclude_files]
            elif not isinstance(exclude_files, list):
                LOG.error("invalid exclude_files type. (exclude_files: %r)",
                          exclude_files)
                exclude_files = []

            for x in exclude_files:
                pattern = helpers.load_patterns_from_file(x)
                if not pattern:
                    raise DWhoConfigurationError("unable to load exclude patterns from %r." % x)

                self.exclude_patterns.update(pattern)

        if self.exclude_patterns:
            self.exclude_patterns = pyinotify.ExcludeFilter(list(self.exclude_patterns))
        else:
            self.exclude_patterns = None

    def _parse_time_opt(self, value, utc = False):
        if value == 'start':
            if utc:
                return datetime.datetime.utcnow()
            else:
                return datetime.datetime.now()
        elif isinstance(value, dict) and 'when' in value:
            xtime = self._parse_time_opt(value['when'], utc)

            if isinstance(xtime, datetime.datetime):
                if 'args' in value:
                    return datetime.timedelta(*value['args']) + xtime
                elif 'kwargs' in value:
                    return datetime.timedelta(**value['kwargs']) + xtime

            return xtime

    def _get_info(self, status):
        return {'caller':     self.caller,
                'caller_id':  self.caller_id,
                'status':     status,
                'started_at': self.started_at,
                'ended_at':   None,
                'errors':     [],
                'path':       self.xpath}

    def run(self):
        xvars   = {}
        options = self.options.copy()
        plugins = self.plugins.copy()

        if 'vars' in options:
            xvars = options.pop('vars') or {}

        if not options['format']:
            xpath = self.xpath
        else:
            fkwargs = {'env': os.environ,
                       'gmtime': datetime.utcnow(),
                       'time': datetime.now(),
                       'vars': xvars}
            xpath = self.xpath.format(**fkwargs)

        if not os.path.exists(xpath):
            LOG.error("path doesn't exist: %r", xpath)
            return

        for opts in plugins.itervalues():
            if '__time__' in opts:
                opts['__time__'] = self._parse_time_opt(opts['__time__'])

            if '__gmtime__' in opts:
                opts['__gmtime__'] = self.parse_time_opt(opts['__gmtime__'], True)

        (last_cfg_path, last_filepath) = (None, None)

        for root, dirs, files in os.walk(xpath, topdown = True):
            if _KILLED:
                return

            if self.exclude_patterns and self.exclude_patterns(root):
                dirs[:] = []
                LOG.debug("exclude path from scan. (path: %r)", root)
                continue

            for filename in files:
                if _KILLED:
                    return

                filepath = os.path.join(root, filename)

                if self.exclude_patterns and self.exclude_patterns(filepath):
                    LOG.debug("exclude file from scan. (filepath: %r)", filepath)
                    continue

                event     = SosBackupsScanEven(filepath, self.caller, self.caller_id, plugins)
                cfg_path  = self.inotify.get_cfg_path(event.pathname)
                if cfg_path:
                    last_cfg_path = cfg_path
                    last_filepath = filepath
                    self.handler.call_plugins(cfg_path, event, include_plugins = self.include_plugins)

        if last_cfg_path and last_filepath:
            event = SosBackupsScanFinishEven(last_filepath, self.caller, self.caller_id, plugins)
            self.handler.call_plugins(last_cfg_path, event, include_plugins = self.include_plugins)

    def __call__(self):
        self.started_at = time.strftime(_DATE_FORMAT)
        DWHO_SHARED.set('sosbackups',
                        self.caller_id,
                        self._get_info('processing'))

        try:
            self.run()
        except Exception, e:
            LOG.exception(e)
            state = DWHO_SHARED.get('sosbackups', self.caller_id)
            if state and 'errors' in state:
                state['errors'].append({'error': repr(e)})

        return self.name


class SosBackupsCronSyncThread(threading.Thread):
    def __init__(self, cron_pool, tabs):
        threading.Thread.__init__(self)
        self.cron_pool = cron_pool
        self.tabs      = tabs
        self.runners   = []
        self.history   = {}

    def callback(self, name):
        if name in self.runners:
            self.runners.remove(name)

    def run(self):
        while not _KILLED:
            for tab, paths in self.tabs.iteritems():
                x = paths
                if isinstance(paths, basestring):
                    x = [{'path': paths}]

                for params in x:
                    options = params.copy()
                    xpath   = options.pop('path')
                    name    = "%s:%s" % (tab, xpath)

                    if name not in self.history:
                        self.history[name] = []

                    if name in self.runners:
                        continue

                    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

                    if t in self.history[name]:
                        if len(self.history[name]) > 120:
                            del self.history[name][0:120]
                        continue

                    self.history[name].append(t)

                    i = croniter(tab, datetime.datetime.now())
                    p = i.get_prev(datetime.datetime).strftime('%Y-%m-%d %H:%M')
                    n = i.get_next(datetime.datetime).strftime('%Y-%m-%d %H:%M')

                    if t in (p, n):
                        self.runners.append(name)
                        self.cron_pool.run(SosBackupsCronScan(name, xpath, options), self.callback)

            time.sleep(1)


class SosBackupsCronSyncPlugin(DWhoPluginBase):
    PLUGIN_NAME = 'cronsync'

    def safe_init(self):
        self.tabs      = self.plugconf['tabs']
        self.cron_pool = workerpool.WorkerPool(max_workers = int(self.plugconf.get('max_workers') or 1),
                                               life_time   = self.plugconf.get('worker_lifetime', WORKER_LIFETIME),
                                               name        = 'cron_pool')
        self.cron_sync = SosBackupsCronSyncThread(self.cron_pool, self.tabs)
        self.cron_sync.daemon = True

    def at_start(self):
        self.cron_sync.start()

    def at_stop(self):
        global _KILLED
        _KILLED = True

        if self.cron_pool:
            self.cron_pool.killall(1)


if __name__ != "__main__":
    def _start():
        PLUGINS.register(SosBackupsCronSyncPlugin())
    _start()
