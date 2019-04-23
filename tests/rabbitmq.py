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
import time
import unittest

import pika
from pika.adapters.blocking_connection import BlockingChannel


class TestRabbitMQ(unittest.TestCase):
    EXCHANGE_NAME = "test_direct"

    def test_publish(self):
        # open connection to rabbit queue
        credentials = pika.PlainCredentials("carbon", "carbon")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="172.17.0.2", virtual_host="/carbon", credentials=credentials
        ))

        # open channel and exchange
        channel: BlockingChannel = connection.channel()
        channel.exchange_declare(
            exchange=self.EXCHANGE_NAME, exchange_type="direct", durable=True
        )

        def return_callback(c, m, p, b):
            print("callback!")

        channel.add_on_return_callback(return_callback)
        # channel.queue_bind(exchange=self.EXCHANGE_NAME, queue="test_queue", routing_key="red")
        # channel.queue_bind(exchange=self.EXCHANGE_NAME, queue="test_queue", routing_key="green")
        channel.basic_publish(
            exchange=self.EXCHANGE_NAME, routing_key="unknown", body="Unknown Tag",
            mandatory=True
        )
        # channel.basic_publish(
        #     exchange=self.EXCHANGE_NAME, routing_key="green", body="[green] green-message"
        # )
        # time.sleep(5)
        # close connection
        channel.close()
        connection.close()

    def test_consumer(self):
        credentials = pika.PlainCredentials("carbon", "carbon")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="localhost", virtual_host="carbon", credentials=credentials
        ))
        channel: BlockingChannel = connection.channel()
        channel.exchange_declare(
            exchange="topic_logs", exchange_type="topic"
        )

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        print("[*] queue name: {}".format(queue_name))

        channel.queue_bind(
            exchange="topic_logs", queue=queue_name, routing_key="daily.*"
        )

        def callback(ch, method, properties, body):
            print("[x] {}:{}".format(method.routing_key, body))

        channel.basic_consume(queue=queue_name, on_message_callback=callback)
        channel.start_consuming()

    def test_single_get(self):
        credentials = pika.PlainCredentials("carbon", "carbon")
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="172.17.0.2", virtual_host="/carbon", credentials=credentials
        ))
        channel: BlockingChannel = connection.channel()

        # basic_get 方法，没有callback参数也ok
        result = channel.basic_get("test_queue")
        print(result)


if __name__ == '__main__':
    unittest.main()
