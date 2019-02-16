#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    class path
    ~~~~~~~~~~~~~~~
    Class description.

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

# 把defaults中的配置全部加载进来
import sys

from .defaults import *

# 根据环境变量加载不同的配置文件
_env = os.getenv("CARBON_ENV", None)
if _env is None:
    print("未设置环境变量CARBON_ENV，默认使用prod配置")
    _env = "prod"
else:
    _env = _env.lower()

try:
    if _env == "dev":
        from .dev import *
    elif _env == "pre":
        from .pre import *
    elif _env == "prod":
        from .prod import *
    else:
        print("未知的启动环境: {env}".format(env=_env))
        sys.exit(1)
except ImportError:
    print("无法加载指定配置文件：{basedir}/carbon/settings/{config_name}.py".format(basedir=BASE_DIR, config_name=_env))
    sys.exit(1)


sk_exists = 'SECRET_KEY' in locals() or 'SECRET_KEY' in globals()
if not sk_exists or not SECRET_KEY:
    print("请设置SECRET_KEY!")
    sys.exit(1)
