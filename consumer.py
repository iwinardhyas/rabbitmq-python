# # consumer.py
# # Consume RabbitMQ queue

# import pika
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "12345")))
# channel = connection.channel()

# def callback(ch, method, properties, body):
#     print(f'{body} is received')
    
# channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
# channel.start_consuming()

#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='sigma', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='sigma', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    # data = json.loads(body.decode("utf-8"))
    # print(data['msisdn'])
    # print(data['nd'])

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
