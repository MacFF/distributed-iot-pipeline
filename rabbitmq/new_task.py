#!/usr/bin/env python
import pika, json, sys

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters(
    host="localhost", port=5672, credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
print("Connected successfully!")

channel.queue_declare(queue="task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
)
print(f" [x] Sent {message}")
connection.close()
# shell 3
# python services/emit_log.py First message......
# python services/emit_log.py Second message..
# python services/emit_log.py Third message......
# python services/emit_log.py Fourth message..
# python services/emit_log.py Fifth message......