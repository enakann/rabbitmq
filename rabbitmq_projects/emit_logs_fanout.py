#!/usr/bin/python

import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')


message = "test_message_new"


channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" Message: {} sent".format(message))
