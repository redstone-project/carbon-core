#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.constant.task
    ~~~~~~~~~~~~~~~~~~~~~~~

    task相关的常量

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""


class TaskType:
    """
    task的类型，包括日常任务和一次性任务
    """
    ONCE_PORT = 0x01
    ONCE_SUB_DOMAIN = 0x02
    ONCE_BRUTE_DIR = 0x03
    ONCE_WEB_SPIDER = 0x04

    DAILY_PORT = 0x11
    DAILY_SUB_DOMAIN = 0x12
    DAILY_BRUTE_DIR = 0x13
    DAILY_WEB_SPIDER = 0x14


class TaskStatus:
    READY = 0x00
    RUNNING = 0x01
    FINISHED = 0x02
    ERROR = 0x03
