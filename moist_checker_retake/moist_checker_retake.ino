#include<MsTimer2.h>
#define sensor 1
#define pomp 3

int rate = 0;
int check =0;
int power = 0;
int wall = 300;
int goal = 600;
unsigned long timer = 0;
const unsigned long interval = 1000;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(pomp,OUTPUT);

MsTimer2::set(1,wall_check);
MsTimer2::start();
}

void loop() {
  // put your main code here, to run repeatedly:

  timer = millis();
  if(timer % interval == 0){
    rate = analogRead(sensor);
    Serial.println(rate);
    Serial.println(check);
    if(rate < wall){
      digitalWrite(pomp,HIGH);
      power = 1;
    }
    if(goal < rate && power != 0){
      digitalWrite(pomp,LOW);
      power = 0;
    }
  }
}


void wall_check(){
  check = Serial.read();
  if(Serial.available()){
    wall = Serial.read();
    goal = wall + 300;
  }
}
