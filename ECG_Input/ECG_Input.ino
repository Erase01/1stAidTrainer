
const byte L0p = 10;
const byte L0m = 11;

void setup() {
  Serial.begin(9600);
  pinMode(L0p, INPUT);   // Setup for leads off detection L0 +
  pinMode(L0m, INPUT);   // Setup for leads off detection L0 -

}

void loop() {
  if((digitalRead(10) == 1) || (digitalRead(11) == 1)) {
    Serial.println('!');
  }
  else {
    Serial.println(analogRead(A0));
  }
  delay(1);
}