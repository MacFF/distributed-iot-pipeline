#!/usr/bin/env python3
"""Test script to demonstrate durable queue behavior"""

import pika


def test_queue_durable():
    """Test 1: Create durable queue"""
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # สร้าง durable queue
    channel.queue_declare(queue="test_durable_queue", durable=True)

    # ส่ง message ที่ persistent
    channel.basic_publish(
        exchange="",
        routing_key="test_durable_queue",
        body="Test message",
        properties=pika.BasicProperties(delivery_mode=2),
    )

    print("✅ Durable queue 'test_durable_queue' created with persistent message")

    # ตรวจสอบ queue ที่สร้าง
    method = channel.queue_declare(queue="test_durable_queue", passive=True)
    message_count = method.method.message_count
    print(f"📨 Messages in queue: {message_count}")

    connection.close()


def test_queue_non_durable():
    """Test 2: Create non-durable queue"""
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # สร้าง non-durable queue
    channel.queue_declare(queue="test_non_durable_queue", durable=False)

    # ส่ง message ที่ non-persistent
    channel.basic_publish(
        exchange="", routing_key="test_non_durable_queue", body="Test message"
    )

    print("✅ Non-durable queue 'test_non_durable_queue' created")

    connection.close()


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Queue Durability in RabbitMQ")
    print("=" * 60)
    test_queue_durable()
    test_queue_non_durable()
    print("=" * 60)
    print("\n💡 คำแนะนำ:")
    print("   - Durable Queue จะอยู่รอด RabbitMQ restart")
    print("   - แต่จะถูกลบถ้าเราลบทิ้ง explicit ผ่าน UI/code")
    print("   - Durable Queue ≠ Permanent/Forever queue")
