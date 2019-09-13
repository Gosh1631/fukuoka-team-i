#include<MsTimer2.h>
#define sensor 1
#define pomp 3

int rate = 0;
int check =0;
unsigned long timer = 0;
const unsigned long interval = 500;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(pomp,OUTPUT);

MsTimer2::set(1000,pomp_work);
MsTimer2::start();
}

void loop() {
  // put your main code here, to run repeatedly:

  timer = millis();
  if(timer % interval == 0){
  moist_read();
  }
}

void moist_read(){
  rate = analogRead(sensor);
  Serial.println(rate);
}


void pomp_work(){
  check = Serial.read();
  if(check==1){
    digitalWrite(pomp,HIGH);
  }
  else{
    digitalWrite(pomp,LOW);
  }
}
