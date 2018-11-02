import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

def callback(ch,method,properties,body):
    origin=properties.headers['x-first-death-queue']
    reason=properties.headers['x-first-death-reason']
    t=properties.headers['x-death'][0]['time']
    print( "received data  --->{} from queue \"{}\" failed due to \"{}\" at  {}".format(body,origin,reason,t))




channel.basic_consume(callback,queue='dead.letter.queue',
                      no_ack=False)

channel.start_consuming()
