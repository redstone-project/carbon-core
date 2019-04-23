#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.settings.config_example
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    示例配置文件

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

DEBUG = True
SECRET_KEY = ""  # 推荐使用该方法生成：base64.b64encode(os.urandom(32))
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CSRF_COOKIE_SAMESITE = None

# LOG相关配置
LOG_TO_FILE = True
LOG_PATH = "./logs/"
LOG_FILENAME = "carbon-core.log"

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carbon',
        'USER': 'carbon',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# RabbitMQ 队列相关配置
RABBIT_VHOST = "/carbon"
RABBIT_USERNAME = "carbon"
RABBIT_PASSWORD = "carbon"
RABBIT_HOST = "localhost"

CYCLE_DAILY_SUFFIX = ".daily"
CYCLE_ONCE_SUFFIX = ".once"

RABBIT_TASK_QUEUES_INFO = {
    "task_port": {
        "name": "task.port",
        "routing_key": "key.port"
    },
    "task_subdomain": {
        "name": "task.subdomain",
        "routing_key": "key.subdomain",
    },
    "task_brutedir": {
        "name": "task.brutedir",
        "routing_key": "key.brutedir",
    },
    "task_spider": {
        "name": "task.spider",
        "routing_key": "key.spider",
    },
    "task_attack": {
        "name": "task.attack",
        "routing_key": "key.attack",
    }
}

RABBIT_RESULT_QUEUES_INFO = {
    "result": {
        "name": "result",
        "routing_key": "",
    }
}

RABBIT_EXCHANGES = {
    "task": "exchange.task",
}
