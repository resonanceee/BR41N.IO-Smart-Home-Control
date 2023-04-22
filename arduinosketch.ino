#include <Servo.h>;

Servo servo;

bool ledred = true;
bool ledyel = true;
bool ledgre = false;
bool door = false;

int redpin = 11;
int yelpin = 12;
int grepin = 13;

String buffer = "";

void setup() {
  pinMode(redpin, OUTPUT);
  pinMode(yelpin, OUTPUT);
  pinMode(grepin, OUTPUT);

  // Initialize servo
  servo.attach(10);
  servo.write(15);
  door = false;

  // Initialize serial  
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()) {
    buffer += Serial.read();
    Serial.println(buffer);
    if (buffer == "4849") {
      if (door != false) {
        servo.write(15); 
        door = false;
      } else {
        servo.write(100); 
        door = true;
      }
        
    }
    if(buffer.length() >= 8) {
      buffer = "";
    }
  };
  if (ledred == true) {
    digitalWrite(redpin, HIGH);
  } else {
    digitalWrite(redpin, LOW);
  }
  if (ledyel == true) {
    digitalWrite(yelpin, HIGH);
  } else {
    digitalWrite(yelpin, LOW);
  }
  if (ledgre == true) {
    digitalWrite(grepin, HIGH);
  } else {
    digitalWrite(grepin, LOW);
  }
}
