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


class JobCycle:
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


class JobScanTypes:
    """
    scan_types: 逗号分隔
        - sub_domain 是否爆破子域名
        - port 是否扫描端口
        - spider 是否爬取更多链接
        - attack 是否打payload
        - brute_dir 是否爆破目录
    """
    SUB_DOMAIN = "sub_domain"
    PORT = "port"
    SPIDER = "spider"
    ATTACK = "attack"
    BRUTE_DIR = "brute_dir"
