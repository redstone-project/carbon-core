#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.system.management.commands.run
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    run command
    启动入口点

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Start Carbon application"

    def handle(self, *args, **options):
        pass
