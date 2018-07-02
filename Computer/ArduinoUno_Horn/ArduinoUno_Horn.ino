// Honks the horn 10 times a minute
void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(13, HIGH);   // Honks
  Serial.println("Honk");   // flag sent to python script
  delay(1);
  Serial.println(""); 
  delay(500);
  digitalWrite(13, LOW);
  delay(5500);
}
