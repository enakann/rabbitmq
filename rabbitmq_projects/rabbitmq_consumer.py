import puka

# declare send and receive clients, both connecting to the same server on local machine
consumer = puka.Client("amqp://localhost/")


# connect sending party

#import pdb;pdb.set_trace()

# connect receiving party
receive_promise = consumer.connect()
consumer.wait(receive_promise)


# declare queue (queue must exist before it is being used - otherwise messages sent to that queue will be discarded)

# start waiting for messages, also those sent before (!), on the queue named rabbit
receive_promise = consumer.basic_consume(queue='rabbit', no_ack=True)

print "Starting receiving!"
#import pdb;pdb.set_trace()

while True:
    received_message = consumer.wait(receive_promise)
    print "GOT: %r" % (received_message['body'],)
