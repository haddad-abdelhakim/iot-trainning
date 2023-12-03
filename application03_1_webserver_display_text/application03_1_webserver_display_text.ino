#include <WiFi.h>
#include <WebServer.h>

// Replace with your network credentials
const char* ssid = "aa";
const char* password = "123123123123";

// Create an instance of the server
WebServer server(80);

// HTML content to be sent when someone accesses the root URL
const char* htmlContent = "<html><body><h1>Hello cr enetcom</h1></body></html>";

// Function to handle the root path
void handleRoot() {
  server.send(200, "text/html", htmlContent);
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

  // Start the server
  server.begin();
}

void loop() {
  // Handle client requests
  server.handleClient();
}
