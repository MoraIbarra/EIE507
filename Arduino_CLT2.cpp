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

RF24 radio(8, 10);

struct SensorData {
  int sensorNumber;
  float temperature;
};

void setup() {
  Serial.begin(9600);

  oneWire[0] = OneWire(SENSOR_PIN_1);
  sensors[0] = DallasTemperature(&oneWire[0]);

  oneWire[1] = OneWire(SENSOR_PIN_2);
  sensors[1] = DallasTemperature(&oneWire[1]);

  oneWire[2] = OneWire(SENSOR_PIN_3);
  sensors[2] = DallasTemperature(&oneWire[2]);

  for (int i = 0; i < NUM_SENSORS; i++) {
    sensors[i].begin();
  }

  radio.begin();
  radio.setPALevel(RF24_PA_HIGH);

  radio.openReadingPipe(0xF0F0F0F0C3LL);

  radio.setDataRate(RF24_250KBPS);

  radio.setPALevel(RF24_PA_HIGH);

  radio.startListening();
}

void loop() {
  if (radio.available()) {
    SensorData data;
    radio.read(&data, sizeof(data));
    Serial.print("Sensor ");
    Serial.print(data.sensorNumber);
    Serial.print(" - Temperature: ");
    Serial.print(data.temperature);
    Serial.println(" °C");
  }
}
