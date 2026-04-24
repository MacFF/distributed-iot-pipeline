import pika, json, sys

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters(
    host="localhost", port=5672, credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
print("Connected successfully!")

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange="direct_logs", routing_key=severity, body=message)
print(f" [x] 1 Sent {severity}:{message}")
connection.close()
