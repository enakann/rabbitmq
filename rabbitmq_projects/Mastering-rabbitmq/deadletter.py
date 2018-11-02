#!/usr/bin/python
import pika
import inspect
import sys

msg=str(sys.argv[1])

def delivered(*args):
    print(args)


print("connecting to rabbitmq broker")
credentials = pika.PlainCredentials('kannan','divya123')
connection=pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-2','5672','/',credentials))

channel=connection.channel()

channel.confirm_delivery()

result=channel.basic_publish(exchange='',routing_key='fibonacci1',mandatory=True,body=msg)

print(result)


#print(inspect.getsource(channel.basic_publish))
#print(inspect.getsourcefile(channel.basic_publish))
#print(arg)

print("done sending")
connection.close()
