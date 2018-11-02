import puka

# declare send and receive clients, both connecting to the same server on local machine
producer = puka.Client("amqp://localhost/")
consumer = puka.Client("amqp://localhost/")


# connect sending party
send_promise = producer.connect()
producer.wait(send_promise)

#import pdb;pdb.set_trace()

# connect receiving party
receive_promise = consumer.connect()
consumer.wait(receive_promise)


# declare queue (queue must exist before it is being used - otherwise messages sent to that queue will be discarded)
send_promise = producer.queue_declare(queue='rabbit')
producer.wait(send_promise)

body="tis is a test message"
# send message to the queue named rabbit

ls=[1,2,3,4,5,6]
send_promise = producer.basic_publish(exchange='', routing_key='rabbit', body=str(ls))
producer.wait(send_promise)

print "Message sent!"

# start waiting for messages, also those sent before (!), on the queue named rabbit
receive_promise = consumer.basic_consume(queue='rabbit', no_ack=True)

print "Starting receiving!"
#import pdb;pdb.set_trace()

while True:
    received_message = consumer.wait(receive_promise)
    print "GOT: %r" % (received_message['body'],)
    break
