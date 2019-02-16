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

import unittest

import pika
from pika.adapters.blocking_connection import BlockingChannel


class TestRabbitMQ(unittest.TestCase):
    def test_publish(self):
        credentials = pika.PlainCredentials("carbon", "carbon")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="localhost", virtual_host="carbon", credentials=credentials
        ))
        channel: BlockingChannel = connection.channel()
        channel.exchange_declare(
            exchange="topic_logs", exchange_type="topic"
        )
        routing_key = "daily.daily_port"
        message = "test queue!"

        channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)
        connection.close()

    # def test_consumer(self):
    #     credentials = pika.PlainCredentials("carbon", "carbon")
    #     connection = pika.BlockingConnection(pika.ConnectionParameters(
    #         host="localhost", virtual_host="carbon", credentials=credentials
    #     ))
    #     channel: BlockingChannel = connection.channel()
    #     channel.exchange_declare(
    #         exchange="topic_logs", exchange_type="topic"
    #     )
    #
    #     result = channel.queue_declare(exclusive=True)
    #     queue_name = result.method.queue
    #     print("[*] queue name: {}".format(queue_name))
    #
    #     channel.queue_bind(
    #         exchange="topic_logs", queue=queue_name, routing_key="daily.*"
    #     )
    #
    #     def callback(ch, method, properties, body):
    #         print("[x] {}:{}".format(method.routing_key, body))
    #
    #     channel.basic_consume(callback, queue=queue_name, no_ack=True)
    #     channel.start_consuming()


if __name__ == '__main__':
    unittest.main()