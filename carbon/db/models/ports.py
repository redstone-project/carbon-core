#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.models.ports
    ~~~~~~~~~~~~~~~~~~~~~~

    端口扫描相关的model


    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models

from ._base import CarbonBaseModel


class PortsManager(models.Manager):
    pass


class CarbonPortsModel(CarbonBaseModel):
    """
    存储端口扫描的结果

    host: 主机
    port_number: 开放的端口号
    protocol: 协议，TCP、UDP
    raw_banner: 原始的banner信息
    service: 识别后的指纹信息
    """
    class Meta:
        db_table = "carbon_ports"

    # task_id，记录是哪个扫描任务发现的该端口，需要关联到任务信息
    host = models.CharField(max_length=16, default="255.255.255.255")
    port_number = models.IntegerField(default=0)
    protocol = models.CharField(max_length=4, default="null")
    raw_banner = models.TextField()
    service = models.TextField()

    objects = models.Manager()
    instance = PortsManager()
