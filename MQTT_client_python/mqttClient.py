# install  paho-mqtt library:    pip install paho-mqtt
import paho.mqtt.client as mqtt
import time

# Define MQTT broker details
broker_address = "localhost"  # Replace with your broker's address
port = 1883  # Default MQTT port
topic_sub = "fromesp/topic"  # Topic to subscribe to
topic_pub = "frompc/topic"  # Topic to  publish to

# Define callbacks for different MQTT events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic_sub)
    else:
        print("Failed to connect, return code: ", rc)

def on_message(client, userdata, msg):
    print("Received message: ", str(msg.payload.decode("utf-8")))

def on_publish(client, userdata, mid):
    print("Message published with mid: ", mid)

# Create MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Connect to MQTT broker
client.connect(broker_address, port=port)

# Start the MQTT loop
client.loop_start()

# Publish messages every 5 seconds
try:
    while True:
        message = "Hello, MQTT!"
        client.publish(topic_pub, message)
        print(f"Published message: {message}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nDisconnecting from broker...")
    client.disconnect()
    client.loop_stop()

