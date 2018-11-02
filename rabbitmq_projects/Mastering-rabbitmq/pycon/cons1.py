import pika

def handler(ch,method,properties,body):
    print("----> Handler: {}".format(body))

connection=pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel=connection.channel()

channel.basic_consume(handler,queue='new',no_ack=True)

channel.start_consuming()
