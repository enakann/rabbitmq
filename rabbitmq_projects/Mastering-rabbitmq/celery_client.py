from celery import Celery

app=Celery('pages_celery',broker='amqp://guest@localhost//')

@app.task
def work(msg):
    print(msg)
