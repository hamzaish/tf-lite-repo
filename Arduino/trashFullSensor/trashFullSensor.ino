// #include <Ultrasonic.h>
const int trigPin = 4;
const int echoPin = 5;
const int fullPin = 6;

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(fullPin, OUTPUT);
  digitalWrite(fullPin, LOW);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2;

  Serial.println("Distance: ");
  Serial.println(distance);
  if(distance <= 53){
    digitalWrite(fullPin, HIGH);
    Serial.println("FULL!!");
  }
  else{
    digitalWrite(fullPin, LOW);
  }
}
