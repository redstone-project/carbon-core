#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.models.jobs
    ~~~~~~~~~~~~~~~~~~~~~

    存储job的mode，每个job代表一个完整的扫描任务
    其中可能包含多个不同的task

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models

from ._base import CarbonBaseModel


class JobManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=0)


class CarbonJobsModel(CarbonBaseModel):
    """
    存储用户提交的作业

    一次性任务使用单独的任务队列
    周期性任务和持续任务共用另外一个任务队列
    保证一次性任务可以立即执行，另外的任务只有在空闲的情况下才会执行

    job_type: 作业类型，一次性任务、持续任务
                - 一次性任务：只执行一次，用于正常扫描
                - 日常任务：一旦完成扫描，马上产生一个相同的任务压入队列中
    payloads: 用户输入的内容，一个目标一行，会自动产生多个task插入表中
    status: job的运行状态，日常任务除非手工停止，否则一直处于Running状态
            - 0x00 Ready
            - 0x01 Prepare
            - 0x02 Queue
            - 0x03 Running
            - 0x04 Finished
            - 0x05 Error
    """
    class Meta:
        db_table = "carbon_jobs"

    job_type = models.IntegerField(default=0)
    payloads = models.TextField()
    status = models.IntegerField(default=0)

    objects = models.Manager()
    instance = JobManager()
