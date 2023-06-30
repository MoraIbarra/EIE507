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

struct RaspiData {
  int sens;
  float temp;
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


  for (int i = 0; i < NUM_SENSORS; i++) {
    sensors[i].begin();
  }

  radio.begin();
  radio.setPALevel(RF24_PA_HIGH);

  radio.openReadingPipe(1, 0xF0F0F0F0E1LL); 
  radio.openReadingPipe(2, 0xF0F0F0F0C3LL);
  
  radio.setDataRate(RF24_250KBPS);

  radio.setPALevel(RF24_PA_HIGH);

  radio.startListening();
}
void loop() {
  
  if (radio.available()) {
    // Read the sensor information
    SensorData data;
    radio.read(&data, sizeof(data));

    RaspiData Raspi[10];

    Raspi[data.sensorNumber].sens = data.sensorNumber;
    Raspi[data.sensorNumber].temp = data.temperature;

if (data.sensorNumber == 6){
  for (int i = 0; i < NUM_SENSORS; i++) {
    sensors[i].requestTemperatures();
    float temperature = sensors[i].getTempCByIndex(0);
    
    Raspi[i+7].sens = i+7;
    Raspi[i+7].temp = temperature;
    if (i == 2){
      for (int i = 0; i < 10; i++){
        Serial.print( Raspi[i].temp);
        Serial.println();
      }
    }
  }
  }
  }
}
