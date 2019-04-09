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
    task的类型
    """
    PORT = 0x0001
    SUB_DOMAIN = 0x0002
    BRUTE_DIR = 0x0003
    WEB_SPIDER = 0x0004
    ATTACK = 0x0005


class TaskStatus:
    READY = 0x00
    RUNNING = 0x01
    FINISHED = 0x02
    ERROR = 0x03
