import pika, json, sys

credentials = pika.PlainCredentials("mikelopster", "password")
parameters = pika.ConnectionParameters(
    host="localhost", port=5672, credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
print("Connected successfully!")

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
print(f"queue_name: {queue_name}")

channel.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
