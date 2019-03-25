#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.core.engines.disassemble
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert job to task

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""

from silex.engines.thread import ThreadEngine

from carbon.utils.logger import logger


class DisassembleEngine(ThreadEngine):
    def __init__(self, app_ctx, name):
        super(DisassembleEngine, self).__init__(app_ctx, name)

    def _worker(self):
        logger.info("{} start!".format(self.name))

        while self.is_running():
            self.ev.wait(1)

        logger.info("{} stop!".format(self.name))
