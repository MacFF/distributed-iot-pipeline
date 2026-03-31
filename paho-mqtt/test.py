import time

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(msg.topic + " +++ " + msg.payload.decode())


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# mqttc.tls_set()
print(f"mqttc: {mqttc}")
print(f"mqttc._protocol: {mqttc._protocol}")
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# mqttc.connect("mqtt.eclipseprojects.io", 8883, 60)
mqttc.connect("broker.hivemq.com", 1883, 60)
# mqttc.connect("localhost", 1883, 60)

print(f"success connect !!!!!!!!!!")
# mqttc.loop_forever()

mqttc.loop_start()

# while True:
for i in range(5):
    # temperature = sensor.blocking_read()
    msq_info = mqttc.publish("paho/test/topic123", "my message22", qos=1)
    msq_info.wait_for_publish()
    print(111111111)

time.sleep(10)
mqttc.loop_stop()
