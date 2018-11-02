#!/usr/bin/python

import pika
import schedule
import time

urls=["http://ebay.to/1G163Lh"]

print(" ***** connecting to RabbitMQ broker ******")

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()

channel.queue_declare(queue='pages')

def produce():
    for url in urls:
        print(" Pushed {}".format(url))
        channel.basic_publish(exchange='',routing_key='pages',body=url)

schedule.every(10).seconds.do(produce)

while True:
    schedule.run_pending()
    time.sleep(1)

connection.close()
