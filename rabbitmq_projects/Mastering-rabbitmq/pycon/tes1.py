import pika
import random

msg="test"+str(random.random())


connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel=connection.channel()

channel.queue_declare(queue='new')

channel.basic_publish(exchange='',routing_key='new',body=msg)
print(msg)
print("done sending")
connection.close()
