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
import urllib.parse
from IPy import IP


def is_url_target(target: str) -> bool:
    """
    判断target是否为合法的URL
    :param target:
    :return:
    """
    target = target.strip()
    if not target.startswith("http://") or not target.startswith("https://"):
        target = "http://" + target

    try:
        result: urllib.parse.ParseResult = urllib.parse.urlparse(target)
        return True if all([result.scheme, result.netloc]) else False
    except ValueError:
        return False


def is_ip_target(target: str) -> bool:
    """
    判断target是否为合法的IP或IP段
    :param target:
    :return:
    """
    try:
        IP(target)
        return True
    except ValueError:
        return False
