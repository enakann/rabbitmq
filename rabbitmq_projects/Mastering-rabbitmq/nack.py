#!/usr/bin/python

import pika

def handler(ch,method,properties,body):
    #print(type(body))
    #if int(body) != 1:
       print("---> Handler: {}".format(body))
       ch.basic_ack(delivery_tag=method.delivery_tag)
    #else:
    #    ch.basic_nack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()
print("channel created")
channel.basic_consume(handler,queue='pages',no_ack=False)
print("queue created")
channel.start_consuming()
print("start consuming")
