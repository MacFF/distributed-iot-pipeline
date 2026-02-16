#!/usr/bin/env python
import pika, sys, os, json


def main():
    credentials = pika.PlainCredentials("mikelopster", "password")
    parameters = pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        # ถ้ามีของมาในคิว hello ให้ส่งมาที่ฟังก์ชัน callback ของฉันด้วย
        print(f" [x] Received {body}")
        data = json.loads(body.decode("utf-8"))

        # 2. ดึงค่าแต่ละตัวออกมาใช้งานตาม Key
        device_id = data.get("device_id")
        temperature = data.get("temp")
        humidity = data.get("hum")

        print(f"ได้รับข้อมูลจาก: {device_id} | อุณหภูมิ: {temperature}°C")

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
