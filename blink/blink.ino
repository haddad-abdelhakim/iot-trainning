// Define the pin number connected to the LED
int ledPin = 23;

// The setup function runs once when you press reset or power the board
void setup() {
  // Initialize the digital pin as an output.
  pinMode(ledPin, OUTPUT);
  
  // Start serial communication at 9600 bits per second
  Serial.begin(9600);
}

// The loop function runs over and over again forever
void loop() {
  // Print a message to the serial monitor
  Serial.println("hi cr enetcom");
  
  // Turn the LED on (HIGH is the voltage level)
  digitalWrite(ledPin, HIGH);
  
  // Wait for 500 milliseconds (half a second)
  delay(500);
  
  // Turn the LED off by making the voltage LOW
  digitalWrite(ledPin, LOW);
  
  // Wait for another 500 milliseconds
  delay(500);
}
