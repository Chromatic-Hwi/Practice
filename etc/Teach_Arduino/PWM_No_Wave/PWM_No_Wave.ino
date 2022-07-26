int PWM1 = 2;
int SW1 = 46;
        
void setup() {
  Serial.begin(9600);
  pinMode(PWM1, OUTPUT);//PWM Out1
  pinMode(SW1, INPUT);
}

void loop() {
  analogWrite(PWM1, 200);
  delay(1000);
  analogWrite(PWM1, 0);
  delay(500);
  if (digitalRead(SW1)==1);{
    analogWrite(PWM1, 100);
    delay(200);
    analogWrite(PWM1, 0);
    delay(200);
    analogWrite(PWM1, 100);
    delay(200);
    analogWrite(PWM1, 0);
    delay(200);
    analogWrite(PWM1, 100);
    delay(200);
    analogWrite(PWM1, 0);
    delay(200);
    analogWrite(PWM1, 100);
    delay(200);
    analogWrite(PWM1, 0);
    delay(200);
    }
}
