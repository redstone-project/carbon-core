#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.models.tasks
    ~~~~~~~~~~~~~~~~~~~~~~

    task相关的model都放在这里

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models

from ._base import CarbonBaseModel


class TasksManager(models.Manager):
    pass


class CarbonTasksModel(CarbonBaseModel):
    """
    记录所有的task信息，task是最小的扫描单元，无法再分割了

    job_id: 记录该task是属于哪一次扫描job的，一个job由多个task组成
    task_type: 任务类型，分为日常任务和普通任务
    payloads: 记录了待扫描的内容，不同的task_type具有不同的格式，但是均为JSON字符串，字段尽可能的保持一致
    status: task的状态
                READY = 0x00        任务创建完成，等待开始
                RUNNING = 0x01      任务执行中
                FINISHED = 0x02     任务正常完成
                ERROR = 0x03        任务异常退出
    """
    class Meta:
        db_table = "carbon_tasks"

    job_id = models.BigIntegerField(default=0)
    task_type = models.CharField(max_length=64, db_index=True)
    payloads = models.TextField()
    status = models.IntegerField(default=0)

    objects = models.Manager()
    instance = TasksManager()