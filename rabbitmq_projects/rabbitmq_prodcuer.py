import puka
import sys

# declare send and receive clients, both connecting to the same server on local machine
producer = puka.Client("amqp://localhost/")


# connect sending party
send_promise = producer.connect()
producer.wait(send_promise)

#import pdb;pdb.set_trace()

# connect receiving party


# declare queue (queue must exist before it is being used - otherwise messages sent to that queue will be discarded)
send_promise = producer.queue_declare(queue='rabbit')
producer.wait(send_promise)

body="tis is a test message"
# send message to the queue named rabbit
i=100000
while i>=0:
 #msg=str(input("please enter the message to be sent --->  ")).strip("\n")
 send_promise = producer.basic_publish(exchange='', routing_key='rabbit', body=str(i))
 producer.wait(send_promise)
 print "Message sent!"
 i-=1


