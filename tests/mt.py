#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    class path
    ~~~~~~~~~~~~~~~~~~

    class desc

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""
import time
from threading import Thread


def worker():
    a = 0
    print("a: {}".format(a))
    a += 1


t1 = Thread(target=worker)
t2 = Thread(target=worker)

t1.start()
time.sleep(1)
t2.start()
