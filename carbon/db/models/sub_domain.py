#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.db.models.sub_domain
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    存储子域名相关的内容

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models

from ._base import CarbonBaseModel


class SubDomainManager(models.Manager):
    pass


class CarbonSubDomainModel(CarbonBaseModel):
    """
    存储子域名爆破的结果

    task_id:
    domain: 子域名
    record_type: 域名解析纪录的类型
                - A 0x01
                - CNAME 0x02
                - AAAA 0x03
    record: 解析记录具体的值
    """
    class Meta:
        db_table = "carbon_sub_domain"

    task_id = models.BigIntegerField(default=0)
    domain = models.CharField(max_length=512, default="")
    record_type = models.IntegerField(default=0)
    record = models.TextField()

    objects = models.Manager()
    instance = SubDomainManager()
