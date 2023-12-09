# iot-trainning

-add json link in file>preferences: Additional Board Manager URLs

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

-check driver and install it: CP2102 or CH340 

-tools>board>boards manager

-search and install: esp32 by expressif 

-select board ESP32 Dev Module

-upload your code

-done :D !



**************************** To install mosquitto: ubuntu ****************************
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients

start mosquitto and test it:
sudo systemctl start mosquitto
sudo systemctl status mosquitto

enable start mosquitto in boot time:
sudo systemctl enable mosquitto

mosquitto config file:
/etc/mosquitto/mosquitto.conf


**************************** To install mosquitto: windows ****************************
mosquitto-2.0.18-install-windows-x64.exe [https://mosquitto.org/files/binary/win64/mosquitto-2.0.18-install-windows-x64.exe] (64-bit build, Windows Vista and up, built with Visual Studio Community 2019)
mosquitto-2.0.18-install-windows-x32.exe [https://mosquitto.org/files/binary/win32/mosquitto-2.0.18-install-windows-x86.exe] (32-bit build, Windows Vista and up, built with Visual Studio Community 2019)

run the installer
Verify the Installation: mosquitto -v

Testing the Broker:
cmd1: mosquitto_sub -h localhost -t test/topic
cmd2: mosquitto_pub -h localhost -t test/topic -m "Hello, MQTT!"

mosquitto config file:
C:\Program Files\mosquitto\mosquitto.conf


****************************  mosquitto config example  ****************************

listener 1883
allow_anonymous false
password_file C:\path\to\your\passwordfile
log_dest file C:\path\to\your\logfile
log_type all

check more [https://mosquitto.org/man/mosquitto-conf-5.html]
