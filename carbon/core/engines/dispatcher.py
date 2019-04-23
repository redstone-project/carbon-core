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
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel
from silex.engines.thread import ThreadEngine

from carbon.db.constant import TaskStatus, JobCycle, TaskType
from carbon.db.models import CarbonTasksModel
from carbon.utils.logger import logger

if typing.TYPE_CHECKING:
    from carbon.application import CarbonMainApplication


class DispatcherEngine(ThreadEngine):
    def __init__(self, name: str, app_ctx: CarbonMainApplication):
        super(DispatcherEngine, self).__init__(name, app_ctx)

        self.app_ctx: CarbonMainApplication = app_ctx

        self.task_exchange: typing.Optional[str] = None

    def init_new_channel(self) -> BlockingChannel:
        # 打开一个channel
        logger.debug("open new channel...")
        channel = self.app_ctx.rabbit_queue.get_new_channel()

        # 定义exchange，如果已经有了则啥都不做
        # durable：设置是否持久化，保证服务器重启交换器不会丢失
        logger.debug("declare exchange...")
        self.task_exchange = settings.RABBIT_EXCHANGES.get("task")
        channel.exchange_declare(
            exchange=self.task_exchange, exchange_type="direct", durable=True
        )

        logger.debug("declare queue...")
        # 定义任务队列，如果队列已经存在了，则什么都不做
        queues = settings.RABBIT_TASK_QUEUES_INFO
        for k, queue_info in queues:
            # 声明 queue
            queue_name = queue_info.get("name")
            daily_queue_name = "{}{}".format(queue_name, settings.CYCLE_DAILY_SUFFIX)
            once_queue_name = "{}{}".format(queue_name, settings.CYCLE_ONCE_SUFFIX)
            logger.debug("declare queue '{}' and '{}'".format(daily_queue_name, once_queue_name))
            channel.queue_declare(queue=once_queue_name, durable=True)
            channel.queue_declare(queue=daily_queue_name, durable=True)

            # 绑定 exchange 和 queue
            routing_key = queue_info.get("routing_key")
            daily_routing_key = "{}{}".format(routing_key, settings.CYCLE_DAILY_SUFFIX)
            once_routing_key = "{}{}".format(routing_key, settings.CYCLE_ONCE_SUFFIX)
            logger.debug(
                "binding queue to exchange, {} -> {} use key: {}".format(queue_name, self.task_exchange, routing_key))
            channel.queue_bind(queue=once_queue_name, exchange=self.task_exchange, routing_key=once_routing_key)
            channel.queue_bind(queue=daily_queue_name, exchange=self.task_exchange, routing_key=daily_routing_key)

        return channel

    def _worker(self):
        logger.info("{} start.".format(self.name))

        # 初始化channel
        channel: BlockingChannel = self.init_new_channel()
        logger.debug("channel id: {}", id(channel))

        while self.is_running():
            # 从数据库中取出所有的READY状态的TASK
            ready_tasks = CarbonTasksModel.instance.get_all_tasks_by_status(TaskStatus.READY)
            if not ready_tasks:
                self.ev.wait(1)
                continue
            logger.debug("Total {} ready tasks in DB.".format(len(ready_tasks)))

            # 将TASK放到队列中
            for _task in ready_tasks:

                # TODO: 跳过attack的任务，需要在receiver的部分下发
                # 现在先把所有的payload都打一遍
                pass

                # 拼出routing_key
                routing_key = _task.build_routing_key()

                # 消息优先级
                msg_properties = BasicProperties(priority=_task.priority)

                # 消息内容
                msg_body = _task.build_message_body()

                # 发送消息到队列中
                channel.basic_publish(
                    exchange=self.task_exchange, routing_key=routing_key, body=msg_body, properties=msg_properties
                )

        logger.info("{} stop.".format(self.name))
