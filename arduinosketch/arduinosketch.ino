#include <Servo.h>;
Servo servo;

int led1pin = 13;
int led2pin = 12;
int doorpin = 11;

bool led1 = false;
bool led2 = false;
bool door = false;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.

  Serial.begin(9600); // Begen listening on port 9600 for serial
  
  servo.attach(doorpin);

  pinMode(led1pin, OUTPUT);
  pinMode(led2pin, OUTPUT);

}

// the loop function runs over and over again forever
void loop() {

   if(Serial.available() > 0)
    {
      char ReaderFromNode;
      ReaderFromNode = (char) Serial.read();
      convertToState(ReaderFromNode); 
    }
    
  if (led1) {
    digitalWrite(led1pin, HIGH);
  } else {
    digitalWrite(led1pin, LOW);
  }

  if (led2) {
    digitalWrite(led2pin, HIGH);
  } else {
    digitalWrite(led2pin, LOW);
  }

  if (door) {
    servo.write(100);
  } else {
    servo.write(20);
  }
}

void convertToState(char chr) {
  Serial.println(chr);
  if(chr=='q'){
    if (led1 == true) {
      led1 = false;
    } else {
      led1 = true;
    }
  }
  if(chr=='w') {
    if (led2 == true) {
      led2 = false;
    } else { 
      led2 = true;
    }
  }
  if(chr=='d'){
    if (door == false) {
      door = true;
    } else {
      door = false;
    }
  }
}