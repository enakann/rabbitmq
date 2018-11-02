#!/usr/bin/python

import pika
from timeout import timeout
from time import sleep


@timeout(30)
def fib(n):
    print("recieved input is {}".format(n))
    try:
      res=[x**x**x for x in range(n)]
    except Exception as e:
        raise e
    return res



def handler(ch,method,properties,body):
    try:
      res=fib(int(body))
    except Exception as e:
        print("*****For Input {} Error Occured is: {}*********".format(body,e))
        res=None
    if res:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        ch.basic_nack(delivery_tag=method.delivery_tag)
    print("---> Result: {}".format(res))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()
print("channel created")
channel.basic_consume(handler,queue='fibonacci',no_ack=False)
print("queue created")
channel.start_consuming()
print("start consuming")
