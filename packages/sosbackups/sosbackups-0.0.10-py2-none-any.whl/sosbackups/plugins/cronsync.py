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


import logging
import os
import threading
import time

from croniter import croniter
from datetime import datetime
from dwho.config import DWHO_SHARED
from dwho.classes.inotify import DWhoInotifyEventHandler
from dwho.classes.plugins import DWhoPluginBase, PLUGINS
from sonicprobe.libs import workerpool


LOG             = logging.getLogger('sosbackups.plugins.cronsync')
_KILLED         = False
WORKER_LIFETIME = 300


class SosBackupsScanEven(object):
    def __init__(self, pathname, options = None):
        self.pathname = pathname
        self.dir      = os.path.isdir(pathname)
        self.mask     = 0
        self.maskname = 'SB_IN_SCAN'
        self.options  = options


class SosBackupsCronScan(threading.Thread):
    def __init__(self, name, xpath, options = None):
        threading.Thread.__init__(self)

        self.name    = name
        self.xpath   = xpath
        self.options = options
        self.inotify = DWHO_SHARED.get('sosbackups', 'inotify')
        self.handler = DWhoInotifyEventHandler(dw_inotify = self.inotify)

    def run(self):
        options = self.options.copy()

        if 'vars' in options:
            xvars = options.pop('vars')
        else:
            xvars = {}

        if 'format' in options:
            xformat = options.pop('format')
        else:
            xformat = False

        if 'plugins' in options:
            plugins = options.pop('plugins')
        else:
            plugins = []

        if not xformat:
            xpath = self.xpath
        else:
            fkwargs = {'env': os.environ,
                       'gmtime': datetime.utcnow(),
                       'time': datetime.now(),
                       'vars': xvars or {}}
            xpath = self.xpath.format(**fkwargs)

        if not os.path.exists(xpath):
            LOG.error("path doesn't exist: %r", xpath)
            return self.name

        if options.get('copyargs'):
            if options['copyargs'].get('time') == 'start':
                options['copyargs']['time'] = datetime.now()

        for root, dirs, files in os.walk(xpath):
            if _KILLED:
                return self.name

            for filename in files:
                if _KILLED:
                    return self.name

                event    = SosBackupsScanEven(os.path.join(root, filename), options)
                cfg_path = self.inotify.get_cfg_path(event.pathname)
                if cfg_path:
                    self.handler.call_plugins(cfg_path, event, include_plugins = plugins)

        return self.name

    def __call__(self):
        try:
            self.run()
        except Exception, e:
            LOG.exception(e)
        finally:
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

                    t = datetime.now().strftime('%Y-%m-%d %H:%M')

                    if t in self.history[name]:
                        if len(self.history[name]) > 120:
                            del self.history[name][0:120]
                        continue

                    self.history[name].append(t)

                    i = croniter(tab, datetime.now())
                    p = i.get_prev(datetime).strftime('%Y-%m-%d %H:%M')
                    n = i.get_next(datetime).strftime('%Y-%m-%d %H:%M')

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
