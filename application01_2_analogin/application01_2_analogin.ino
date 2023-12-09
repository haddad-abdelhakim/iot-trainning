void setup() {
  Serial.begin(9600); // Start the Serial communication
  analogReadResolution(12); // Set the resolution to 12-bit (0 - 4095)
}

void loop() {
  int sensorValue = analogRead(34); // Read the input on ADC1_CHANNEL_6 (GPIO34)
  Serial.println(sensorValue); // Print the value to the Serial Monitor
  delay(1000); // Wait for a second
}
