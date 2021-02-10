void setup() {

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = analogRead(A0);
  // Convert the reading into voltage:
  float voltage = reading * (5000 / 1024.0);
  // Convert the voltage into the temperature in degree Celsius:
  float temperature = voltage / 10;
  // Print the temperature in the Serial Monitor:
  Serial.println(temperature);
  delay(1000); // wait a second between readings
}
