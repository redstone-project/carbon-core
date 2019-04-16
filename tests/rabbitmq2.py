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
import pika
from django.conf import settings
from pika.adapters.blocking_connection import BlockingChannel

EXCHANGE_NAME = "test_direct"


def test_publish():
    # open connection to rabbit queue
    credentials = pika.PlainCredentials("carbon", "carbon")
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="172.17.0.2", virtual_host="/carbon", credentials=credentials
    ))

    # open channel and exchange
    channel: BlockingChannel = connection.channel()
    channel.confirm_delivery()
    channel.exchange_declare(
        exchange=settings.rabbit, exchange_type="direct", durable=True
    )

    def return_callback(c, m, p, b):
        print("callback!")

    channel.add_on_return_callback(return_callback)
    # channel.queue_bind(exchange=self.EXCHANGE_NAME, queue="test_queue", routing_key="red")
    # channel.queue_bind(exchange=self.EXCHANGE_NAME, queue="test_queue", routing_key="green")
    channel.basic_publish(
        exchange=EXCHANGE_NAME, routing_key="unknown", body="Unknown Tag",
        mandatory=True
    )
    # channel.basic_publish(
    #     exchange=self.EXCHANGE_NAME, routing_key="green", body="[green] green-message"
    # )
    # time.sleep(5)
    # close connection
    channel.close()
    connection.close()


if __name__ == '__main__':
    test_publish()
