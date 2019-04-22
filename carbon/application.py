#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.application
    ~~~~~~~~~~~~~~~~~~

    Core Application Class

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""

import typing

from silex.queue import RabbitQueue
from django.conf import settings


class CarbonMainApplication(object):
    class QUEUES:
        PORT_TASK_DAILY_QUEUE = None
        PORT_TASK_ONCE_QUEUE = None

    def __init__(self):
        super(CarbonMainApplication, self).__init__()

        # rabbit queue 的连接类
        # 需要用到的时候通过get_new_channel获取新的channel使用
        self.rabbit_queue: typing.Optional[RabbitQueue] = None

    def init(self):
        """
        初始化部分，初始化队列，engine等对象
        :return:
        """
        self.rabbit_queue = RabbitQueue()
        self.rabbit_queue.connect(
            settings.RABBIT_USERNAME, settings.RABBIT_PASSWORD, settings.RABBIT_HOST, settings.RABBIT_VHOST
        )

        # 开始声明 exchange 和 queue, 如果已经存在了，则什么都不做
        # channel = self.rabbit_queue.get_new_channel()
        # channel.queue_declare(settings.RABBIT_QUEUES_NAME.get("port_task", "task.port"), durable=True)
        # channel.queue_declare(settings.)

    def run(self):
        """
        启动所有的engine，程序的入口点
        :return:
        """
        pass

    def stop(self):
        """
        结束清理部分
        :return:
        """
        pass
