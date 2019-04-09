#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.constant
    ~~~~~~~~~~~~~~~~~~

    class desc

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""

from .job import JobCycle, JobStatus
from .task import TaskStatus, TaskType


class ProtocolType:
    UDP = "udp"
    TCP = "tcp"


class DNSRecordType:
    A = 0x01
    CNAME = 0x02
    AAAA = 0x03
