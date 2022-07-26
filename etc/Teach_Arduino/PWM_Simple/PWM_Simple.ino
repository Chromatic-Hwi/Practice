int PWM1 = 2;

int SW1 = 46;
        
void setup() {
  Serial.begin(9600);
  pinMode(PWM1, OUTPUT);//PWM Out1
  pinMode(SW1, INPUT);
}

void loop() {
  while(true){
    for(int i=0; i<255; i++){
      analogWrite(PWM1, i);
      Serial.print(i);
      Serial.println(digitalRead(SW1));
      if (digitalRead(SW1)==1);{
        break
        };
      delay(10);   
      }
    for(int i=255; i>0; i--){
      analogWrite(PWM1, i);
      Serial.print(i)
      Serial.println(digitalRead(SW1));
      if (digitalRead(SW1)==1);{
        break
        };
      }
      delay(10);
      }
    println("PWM Signal Stop!")
    delay(3000);
    }
}
