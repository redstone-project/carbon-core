#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.core.engines.receiver
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    接受 Agent 端回报的扫描结果

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""

import typing

from django.conf import settings
from silex.engines.thread import ThreadEngine

from carbon.utils.logger import logger

if typing.TYPE_CHECKING:
    from carbon.application import CarbonMainApplication


class ReceiverEngine(ThreadEngine):
    def __init__(self, name: str, app_ctx: CarbonMainApplication):
        super(ReceiverEngine, self).__init__(app_ctx, name)

        self.app_ctx: CarbonMainApplication = app_ctx

        self.result_exchange: typing.Optional[str] = None

    def _worker(self):
        logger.info("{} start.".format(self.name))

        # 获取一个新的channel
        channel = self.app_ctx.rabbit_queue.get_new_channel()

        # 初始化channel
        result_queue_info = settings.RABBIT_RESULT_QUEUES_INFO.get("result")
        channel.queue_declare(result_queue_info.get("name"), durable=True)
        channel.basic_qos(prefetch_count=1)

        logger.debug("ready for receive result message.")
        while self.is_running():
            channel.basic_get(result_queue_info.get("name"))

        logger.info("{} stop.".format(self.name))
