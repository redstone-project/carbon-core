#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.constant
    ~~~~~~~~~~~~~~~~~~

    记录一些DB字段中的常量信息

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""


# noinspection PyPep8Naming
class JOB_TYPE:
    """
    jobs中的job_type字段使用
    ONCE: 一次性扫描任务
    DAILY: 日常扫描任务，任务完成后会重新生成任务压入到队列中
    """
    ONCE = 0x01
    DAILY = 0x02


# noinspection PyPep8Naming
class TASK_TYPE:
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


class _STATUS:
    READY = 0x00
    RUNNING = 0x01
    FINISHED = 0x02
    ERROR = 0x03


# noinspection PyPep8Naming
class TASK_STATUS(_STATUS):
    """
    Task的状态常量定义
    """
    pass


# noinspection PyPep8Naming
class JOB_STATUS(_STATUS):
    """
    JOB的状态常量定义
    """
    pass


class PROTOCOL:
    UDP = "udp"
    TCP = "tcp"


# noinspection PyPep8Naming
class DNS_RECORD_TYPE:
    A = 0x01
    CNAME = 0x02
    AAAA = 0x03

