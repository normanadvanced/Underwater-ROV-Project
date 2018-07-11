// Honks the horn 10 times a minute
void setup() {
  pinMode(8, OUTPUT);
  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(8, HIGH);   // Honks
  Serial.println("Honk");   // flag sent to python script
  delay(1);
  Serial.println(""); 
  delay(500);
  digitalWrite(8, LOW);
  delay(5500);
}
