#!/usr/bin/env python
import pika, json

credentials = pika.PlainCredentials("mikelopster", "password")
parameters = pika.ConnectionParameters(
    host="localhost", port=5672, credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
print("Connected successfully!")

channel.queue_declare(queue="hello")

payload = {"device_id": "ESP32-SENSOR-001", "temp": 135.0, "hum": 60}
json_payload = json.dumps(payload)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json_payload)

print(f"type: {type(json_payload)}")
print(f" [x] Sent {json_payload}")
connection.close()

# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World 8!')
