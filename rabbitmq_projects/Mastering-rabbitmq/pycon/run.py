import pika
from producer import *
from consumer import *
from init_rabbitmq import *
def hello_world():
    init_rabbitmq()

    conn=pika.BlockingConnection()
    p=Producer(conn)
    p.send_message("Hello World","pycon","routing.key")

    c=Consumer(conn)

    print(c.get_message("pyq"))



hello_world()
