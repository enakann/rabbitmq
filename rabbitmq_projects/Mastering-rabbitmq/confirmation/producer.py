#!/usr/bin/python
import pika
import inspect
import sys


def on_open(connection):
    channel=connection.channel(on_channel_open)

def on_channel_open(channel):
    channel.confirm_delivery(on_delivery_confirmation)
    channel.basic_publish(exchange='',routing_key='pages',mandatory=True,body=msg)
def on_delivery_confirmation(frame):
    print(frame.method)

msg=str(sys.argv[1])

print("connecting to rabbitmq broker")
credentials = pika.PlainCredentials('kannan','divya123')
connection=pika.SelectConnection(pika.ConnectionParameters('rabbitmq-2','5672','/',credentials),on_open_callback=on_open)


print("done sending")
#connection.close()


