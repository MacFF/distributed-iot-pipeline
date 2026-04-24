import pika, json, sys

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters(
    host="localhost", port=5672, credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
print("Connected successfully!")

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 2 else "anonymous.info"
print(f"sys.argv >>> {sys.argv}")
print(f"routing_key: {routing_key}")
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="topic_logs", routing_key=routing_key, body=message)
print(f" [x] Sent {routing_key}: {message}")
connection.close()
