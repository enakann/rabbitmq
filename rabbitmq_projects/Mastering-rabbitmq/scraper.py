#!/usr/bin/python

import pika
import requests
from BeautifulSoup import BeautifulSoup

def handler(ch,method,properties,url):
    print("starting to fetch {}".format(url))
    r=requests.get(url)
    soup=BeautifulSoup(r.text)
    print("Extracet {}".format(soup.html.head.title))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("Done with url".format(url))

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

print("Handling Messages")

channel.basic_consume(handler,queue='pages',no_ack=False)

channel.start_consuming()
