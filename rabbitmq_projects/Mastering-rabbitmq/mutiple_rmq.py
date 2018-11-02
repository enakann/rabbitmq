import pika

credentials = pika.PlainCredentials('kannan','divya123')

configs = (
    pika.ConnectionParameters('rabbitmq-1','5672','/',credentials),
    pika.ConnectionParameters(('rabbitmq-2','5672','/',credentials),
                              connection_attempts=5, retry_delay=1))
connection = pika.BlockingConnection(configs)
