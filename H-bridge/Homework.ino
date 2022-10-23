
const int IN3 = 5;
const int IN4 = 4;

const int ENA = 9;

void setup() {

  pinMode (IN3, OUTPUT);
  pinMode (IN4, OUTPUT);
  pinMode (9, OUTPUT);

}

void loop() {

  analogWrite(ENA, 255);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  //Controlling speed (0 = off and 255 = max speed):
  analogWrite(9, 100); //ENA pin

}

