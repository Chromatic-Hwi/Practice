#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11
#define LED1 10
#define LED2 12
#define SW1 5
#define SW2 6

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(SW1, INPUT);
  pinMode(SW2, INPUT);
}

void loop() 
{
  char data = Serial.read();

  int sw1;
  int sw2;

  sw1 = digitalRead(SW1);
  sw2 = digitalRead(SW2);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if(sw1 == HIGH && sw2 == HIGH)
  {
    digitalWrite(LED1, HIGH);
    digitalWrite(LED2, HIGH);
    }
  else if(sw1 == HIGH && sw2 == LOW)
  {
    digitalWrite(LED1, HIGH);
    digitalWrite(LED2, LOW);
    }
  else if(sw1 == LOW && sw2 == HIGH)
  {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, HIGH);
    }
  else
  {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    }
    
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
