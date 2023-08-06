# -*- coding: utf-8 -*-
"""copy plugin"""

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

from dwho.classes.inoplugs import INOPLUGS
from sosbackups.classes.rsyncplug import SosBackupsRsyncPlug


LOG = logging.getLogger('sosbackups.plugins.copy')


class SosBackupsCopyInoPlug(SosBackupsRsyncPlug):
    PLUGIN_NAME = 'copy'

    def _path_options(self):
        if not self.cfg_path \
           or self.cfg_path.path not in self.config['inotify']['paths']:
            return

        return self.config['inotify']['paths'][self.cfg_path.path]

    def run(self, cfg_path, event, filepath):
        if not self.plugconf:
            return

        params         = self.plugconf.copy()
        prefix_path    = params.get('prefix_path') or self.prefix_path

        path_format    = params.get('path_format') or '{dst}'
        fkwargs        = {'dst': self.realdstpath(event, filepath, prefix_path),
                          'filepath': filepath,
                          'env': os.environ,
                          'gmtime': datetime.datetime.utcnow(),
                          'time': datetime.datetime.now(),
                          'vars': params.get('vars') or {}}

        if hasattr(event, 'options') \
           and isinstance(event.options, dict) \
           and event.options.get('copyargs'):
            fkwargs.update(event.options.get('copyargs'))

        path_options   = self._path_options()

        if path_options.get('path_format'):
            path_format = path_options['path_format']

        if path_options.get('copyargs'):
            fkwargs.update(path_options.get('copyargs'))

        params['dest'] = path_format.format(**fkwargs)

        self.run_rsync_cmd(params, event, filepath)


if __name__ != "__main__":
    def _start():
        INOPLUGS.register(SosBackupsCopyInoPlug())
    _start()
