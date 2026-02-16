```sh
# MQTT to AMQP Messaging Experiment

This project is an experimental setup to explore message communication using:

- Mosquitto (MQTT Broker)
- paho-mqtt (MQTT Client in Python)
- RabbitMQ (AMQP Broker)
- pika (AMQP Client in Python)

## Objective

To test and demonstrate how messages can be:

1. Published via MQTT
2. Received by a Python subscriber (paho-mqtt)
3. Forwarded to RabbitMQ via AMQP (pika)
4. Consumed from RabbitMQ

## Tech Stack

- Mosquitto (MQTT Broker)
- RabbitMQ (AMQP Broker)
- Python 3.x
- paho-mqtt
- pika
- Docker (optional)

## Message Flow

MQTT Publisher
    ↓
Mosquitto Broker
    ↓
paho-mqtt Subscriber (Python)
    ↓
RabbitMQ (AMQP)
    ↓
AMQP Consumer

## How to Run

1. Start Mosquitto and RabbitMQ
2. Install dependencies:

```