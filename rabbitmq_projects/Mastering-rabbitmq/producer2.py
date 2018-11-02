#!/usr/bin/python
import pika

import sys

msg=str(sys.argv[1])

print("connecting to rabbitmq broker")

params = pika.URLParameters('amqp://kannan:divya123@rabbitmq-1:5672')
connection=pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue='pages')

channel.basic_publish(exchange='',routing_key='pages',body=msg)

print("done sending")
connection.close()
