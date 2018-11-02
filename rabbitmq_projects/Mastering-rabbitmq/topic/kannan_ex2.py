#!/usr/bin/python
import pika
import inspect
import sys


print("connecting to rabbitmq broker")
credentials = pika.PlainCredentials('kannan','divya123')
connection=pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-2','5672','/',credentials))

channel=connection.channel()



result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
for severity in ["kannan.log","log.kannan"]:
    channel.queue_bind(exchange='kannan',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue='kannan1',
                      no_ack=False)

channel.start_consuming()
