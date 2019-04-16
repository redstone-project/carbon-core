#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.core.engines.dispatcher
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    从数据库中读出task

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""
import typing

from django.conf import settings
from silex.engines.process import ProcessEngine

from carbon.utils.logger import logger
from carbon.db.models import CarbonTasksModel
from carbon.db.constant import TaskStatus

if typing.TYPE_CHECKING:
    from carbon.application import CarbonMainApplication


class DispatcherEngine(ProcessEngine):
    def __init__(self, name: str, app_ctx: CarbonMainApplication):
        super(DispatcherEngine, self).__init__(name, app_ctx)

        self.app_ctx: CarbonMainApplication = app_ctx

    def _worker(self):
        logger.info("{} start.".format(self.name))

        # 打开一个channel
        channel = self.app_ctx.rabbit_queue.get_new_channel()
        # 定义exchange，如果已经有了则啥都不做，durable：设置是否持久化，保证服务器重启交换器不会丢失
        channel.exchange_declare(
            exchange=settings.RABBIT_EXCHANGES_NAME.get("task"), exchange_type="direct", durable=True
        )

        # bind exchange 和 queue, TODO:看看这个exchange -> queue的bind能不能通过CLI完成，这样直接命令写到DOCKER里
        channel.exchange_bind()

        while self.is_running():
            # 从数据库中取出所有的READY状态的TASK
            ready_tasks = CarbonTasksModel.instance.get_all_tasks_by_status(TaskStatus.READY)
            if not ready_tasks:
                self.ev.wait(1)
                continue
            logger.debug("Total {} ready tasks in DB.".format(len(ready_tasks)))

            # 将TASK放到队列中

        logger.info("{} stop.".format(self.name))
