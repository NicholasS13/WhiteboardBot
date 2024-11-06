#include "meshota.h"
void setup() {
  // put your setup code here, to run once:
  otaSetup();
}

void loop() {
  // put your main code here, to run repeatedly:
  otaLoop();
  if(Serial.available()){
    String s = Serial.readString();
    if(s.indexOf("update")!=-1)
       mesh.sendBroadcast(s);
  }
}
