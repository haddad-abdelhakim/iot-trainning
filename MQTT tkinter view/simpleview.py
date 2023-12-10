import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT configurations
broker_address = "localhost"  # Change this to your MQTT broker's address
temperature_topic = "team1/temperature"
humidity_topic = "team1/humidity"
onoff_topic = "team1/onoff"

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(temperature_topic)
    client.subscribe(humidity_topic)

def on_message(client, userdata, msg):
    if msg.topic == temperature_topic:
        temperature_value.set(msg.payload.decode() + " °C")
    elif msg.topic == humidity_topic:
        humidity_value.set(msg.payload.decode() + "%")

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker_address, 1883, 60)

# Tkinter GUI setup
root = tk.Tk()
root.title("MQTT Sensor Data")

# Variables to store temperature and humidity values
temperature_value = tk.StringVar()
humidity_value = tk.StringVar()

# Initialize with default values
temperature_value.set("24 °C")
humidity_value.set("40%")

# Font settings
font_style = ("Arial", 24)

# Labels to display temperature and humidity
temperature_label = tk.Label(root, text="Temperature:", font=font_style)
temperature_label.pack()

temperature_display = tk.Label(root, textvariable=temperature_value, font=font_style)
temperature_display.pack()

humidity_label = tk.Label(root, text="Humidity:", font=font_style)
humidity_label.pack()

humidity_display = tk.Label(root, textvariable=humidity_value, font=font_style)
humidity_display.pack()

# Function to start MQTT client loop
def start_mqtt():
    mqtt_client.loop_start()

# Start MQTT client loop when the application starts
start_mqtt()

# Set window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Function to handle button click
def toggle_system():
    if system_state.get() == "ON":
        mqtt_client.publish(onoff_topic, "OFF")
        system_state.set("OFF")
    else:
        mqtt_client.publish(onoff_topic, "ON")
        system_state.set("ON")

# Button to toggle system on/off
system_state = tk.StringVar()
system_state.set("OFF")
toggle_button = tk.Button(root, textvariable=system_state, command=toggle_system, font=font_style)
toggle_button.pack()

# Run the Tkinter main loop
root.mainloop()

