#include <WiFi.h>
#include <WebServer.h>

// Replace with your network credentials
const char* ssid = "aa";
const char* password = "123123123123";

// Create an instance of the server
WebServer server(80);

// HTML content with a text field and a send button
const char* htmlContent = "<html><body><h1>Hello cr enetcom</h1>"
                          "<form action=\"/submit\" method=\"GET\">"
                          "<input type=\"text\" name=\"message\" placeholder=\"Enter message\">"
                          "<input type=\"submit\" value=\"Send\">"
                          "</form></body></html>";

// Function to handle the root path
void handleRoot() {
  server.send(200, "text/html", htmlContent);
}

// Function to handle the form submission
void handleSubmit() {
  String message = server.arg("message");
  Serial.println("Message received in ESP32: " + message);
  server.sendHeader("Location", "/");
  server.send(303); // Redirect back to the root path
}

void setup() {
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  // Print the local IP address
  Serial.println("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

  // Route to handle HTTP GET request for the root path
  server.on("/", handleRoot);

  // Route to handle GET request for form submission
  server.on("/submit", handleSubmit);

  // Start the server
  server.begin();
}

void loop() {
  // Handle client requests
  server.handleClient();
}
