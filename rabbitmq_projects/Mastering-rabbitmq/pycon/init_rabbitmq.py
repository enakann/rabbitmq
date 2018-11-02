import pika
def init_rabbitmq():
    conn=pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    chan=conn.channel()

    chan.exchange_declare(exchange="pycon",exchange_type="direct")
    chan.queue_declare(queue="pyq",durable=True)
    chan.queue_bind(exchange="pycon",queue="pyq",routing_key="routing.key")
    conn.close()


#init_rabbitmq()
