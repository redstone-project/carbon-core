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

import sys
import traceback

from django.core.management import BaseCommand

from carbon.application import CarbonMainApplication
from carbon.core import global_data


class Command(BaseCommand):
    help = "Start Carbon application"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Staring Carbon application..."))

        # 初始化整个App class
        global_data.carbon_application = CarbonMainApplication()
        try:
            global_data.carbon_application.init()
        except Exception as e:
            tbe = traceback.TracebackException(*sys.exc_info())
            error_message = "".join(tbe.format())
            self.stdout.write(
                "Error while initialize carbon application! Exception: {}\nDetails: \n{}".format(e, error_message))

        # 启动app
        try:
            global_data.carbon_application.run()
        except Exception as e:
            tbe = traceback.TracebackException(*sys.exc_info())
            error_message = "".join(tbe.format())
            self.stdout.write(
                "Error while starting carbon application! Exception: {}\nDetails: \n{}".format(e, error_message))
