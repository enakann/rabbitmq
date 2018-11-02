#!/usr/bin/env python
import pika


params = pika.URLParameters('amqp://kannan:divya123@rabbitmq-1:5672')

try:
    connection=pika.BlockingConnection(params)
except pika.exceptions.ConnectionClosed:
    params = pika.URLParameters('amqp://kannan:divya123@rabbitmq-2:5672')
    connection=pika.BlockingConnection(params)


#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
#channel.exchange_declare('events')
#result = channel.queue_declare(exclusive=True)
#queue_name = result.method.queue
#channel.queue_bind(exchange='events',
#                  queue='rpc_queue')
#channel.queue_declare(queue='rpc_queue')

def fib(n):
    #print("fib called")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib1(n):
    return n

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)
    print(props.reply_to)
    res=ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    print(res)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
