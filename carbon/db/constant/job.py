#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.constant.job
    ~~~~~~~~~~~~~~~~~~~~~~

    JOB相关的常量

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""


class JobType:
    """
    jobs中的job_type字段使用
    ONCE: 一次性扫描任务
    DAILY: 日常扫描任务，任务完成后会重新生成任务压入到队列中
    """
    ONCE = 0x01
    DAILY = 0x02


class JobStatus:
    """
        - 0x00 Ready
        - 0x01 Prepare
        - 0x02 Queue
        - 0x03 Running
        - 0x04 Finished
        - 0x05 Error
    """
    READY = 0x00
    PREPARE = 0x01
    QUEUE = 0x02
    RUNNING = 0x03
    FINISHED = 0x04
    ERROR = 0x05
