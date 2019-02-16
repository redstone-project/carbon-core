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


class PROTOCOL:
    TCP = "TCP"
    UDP = "UDP"


# noinspection PyPep8Naming
class TASK_TYPE:
    DAILY_PORT = "daily_port"
    PORT = "port"


# noinspection PyPep8Naming
class TASK_STATUS:
    READY = 0x00
    RUNNING = 0x01
    FINISHED = 0x02
    ERROR = 0x03
