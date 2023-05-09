void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0)); 
}

void loop() {
  int randomNum = random(0, 100);
  Serial.println(randomNum);
  delay(1000);
}
