#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.application
    ~~~~~~~~~~~~~~~~~~

    Core Application Class

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""


class CarbonApplication(object):

    def __init__(self):
        super(CarbonApplication, self).__init__()

    def init(self):
        """
        初始化部分，初始化队列，engine等对象
        :return:
        """
        pass

    def run(self):
        """
        启动所有的engine，程序的入口点
        :return:
        """
        pass

    def stop(self):
        """
        结束清理部分
        :return:
        """
        pass
