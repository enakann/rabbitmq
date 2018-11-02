#!/usr/bin/python

import pika

def handler(ch,method,properties,body):
    #print(ch)
    #print(dir(method))
    #print(dir(properties))
    print("---> Handler: {}".format(body))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()
print("channel created")
channel.basic_consume(handler,queue='pages',no_ack=True)
print("queue created")
channel.start_consuming()
print("start consuming")
