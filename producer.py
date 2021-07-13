# # producer.py
# # This script will publish MQ message to my_exchange MQ exchange

# import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'rabbitmq')))
# channel = connection.channel()

# channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')

# connection.close()

#!/usr/bin/env python
import pika
import sys
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "WhatsApp Video 2021-06-10 at 10.50.58.mp4"
data = {
    'object': 1,
    'file_name': "1231291023012.mp4"
}
message = ' '.join(sys.argv[1:]) or data
channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(data))
print(" [x] Sent %r" % message)
connection.close()
