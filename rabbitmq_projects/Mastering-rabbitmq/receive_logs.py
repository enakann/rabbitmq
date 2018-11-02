#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


print(' [*] Waiting for logs. To exit press CTRL+C')

def fib(n):
    #print("fib called")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    print(fib(int(body)))
    ch.basic_ack(delivery_tag=method.delivery_tag)


#channel.queue_bind(exchange='direct_logs', queue='fibo',
#routing_key='info')

#channel.queue_bind(exchange='direct_logs', routing_key='info')

channel.basic_consume(callback,
                      queue='fibo',
                      no_ack=False)


channel.start_consuming()
