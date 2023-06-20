
#define analog_read_in A0

void setup() {
  Serial.begin(9600);

}

void loop() {
  int fsr_value = analogRead(analog_read_in);
  Serial.print("Force sensor raw data:");
  Serial.println(fsr_value);
  delay(100);
}