#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() 
{
  char data = Serial.read();

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  if(isnan(h) || isnan(t))
  {
    Serial.print("No Data Input");
    Serial.println(",");
    }
  else
  {
    Serial.print("T");
    Serial.print(",");
    Serial.print(t);
    Serial.print(",");
    Serial.print("H");
    Serial.print(",");
    Serial.print(h);
    Serial.println(",");
    }
    delay(200);
    
}
