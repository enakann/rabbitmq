#!/usr/bin/env python
import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.params = pika.URLParameters('amqp://kannan:divya123@rabbitmq-1:5672')
        try:
          self.connection=pika.BlockingConnection(self.params)
        except pika.exceptions.ConnectionClosed:
          self.params = pika.URLParameters('amqp://kannan:divya123@rabbitmq-2:5672')
          self.connection=pika.BlockingConnection(params)

        self.channel = self.connection.channel()
        result = self.channel.queue_declare("output")
        self.callback_queue = result.method.queue
        print(self.callback_queue)

        self.channel.basic_consume(self.on_response, no_ack=False,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        #print("on_response called")
        if self.corr_id == props.correlation_id:
            self.response = body
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        #self.channel.exchange_declare('events')
        self.channel.basic_publish(exchange='events',
                                   routing_key='',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
#import pdb;pdb.set_trace()

val=int(input("please enter a numbe to calculate its fibonaci value -->"))
print(" [x] Requesting fib{}".format(val))
response = fibonacci_rpc.call(val)
print(" [.] Got %r" % response)
