#include <OneWire.h>
#include <DallasTemperature.h>
#include <SPI.h>
#include <RF24.h>

#define SENSOR_PIN_1 2
#define SENSOR_PIN_2 3
#define SENSOR_PIN_3 4

#define NUM_SENSORS 3

OneWire oneWire[NUM_SENSORS];
DallasTemperature sensors[NUM_SENSORS];
// Configuration of the NRF24 module
RF24 radio(9, 10);  // CE and CSN pins, respectively

// Structure to store sensor information
struct SensorData {
  int sensorNumber;
  float temperature;
};

void setup() {
  Serial.begin(9600);

  // Inicializar la comunicación con cada sensor
  oneWire[0] = OneWire(SENSOR_PIN_1);
  sensors[0] = DallasTemperature(&oneWire[0]);

  oneWire[1] = OneWire(SENSOR_PIN_2);
  sensors[1] = DallasTemperature(&oneWire[1]);

  oneWire[2] = OneWire(SENSOR_PIN_3);
  sensors[2] = DallasTemperature(&oneWire[2]);

  // Iniciar la comunicación con los sensores
  for (int i = 0; i < NUM_SENSORS; i++) {
    sensors[i].begin();
  }

  // Initialize the NRF24 module
  radio.begin();
  radio.setPALevel(RF24_PA_HIGH);

  // Configure the reading pipe for channel 1
  radio.openReadingPipe(1, 0xF0F0F0F0E1LL);  // Receiver address (Arduino receiver)
  // Set the transmission speed to 250 kbps
  radio.setDataRate(RF24_250KBPS);

  // Set the transmission power to a high level
  radio.setPALevel(RF24_PA_HIGH);

  // Start listening on channel 1
  radio.startListening();
}

void loop() {
  // Check if there is data available to receive on channel 1
  if (radio.available()) {
    // Read the sensor information
    SensorData data;
    radio.read(&data, sizeof(data));

    // Print the received information from channel 1
    Serial.print("Sensor ");
    Serial.print(data.sensorNumber);
    Serial.print(" - Temperature: ");
    Serial.print(data.temperature);
    Serial.println(" °C");
  }
}
