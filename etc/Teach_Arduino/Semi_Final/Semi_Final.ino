int PWM1 = 2;
int PWM2 = 3;
int PWM3 = 4;
int PWM4 = 5;

int D_OUT =22;
int D_OUT =24;
int D_OUT =26;
int D_OUT =28;

int DIP1 = 47;
int DIP2 = 49;
int DIP3 = 51;
int DIP4 = 53;

int SW1 = 46;
int SW2 = 48;
int SW3 = 50;
int SW4 = 52;
        
void setup() {
  Serial.begin(9600);
  pinMode(PWM1, OUTPUT);//PWM Out1
  pinMode(PWM2, OUTPUT);//PWM Out2
  pinMode(PWM3, OUTPUT);//PWM Out3
  pinMode(PWM4, OUTPUT);//PWM Out4

  pinMode(D_OUT, OUTPUT);//Digital Output1
  pinMode(D_OUT, OUTPUT);//Digital Output2
  pinMode(D_OUT, OUTPUT);//Digital Output3
  pinMode(D_OUT, OUTPUT);//Digital Output4

  pinMode(DIP1, INPUT);//점등 시간 조정을 위한 2진 자리1
  pinMode(DIP2, INPUT);//점등 시간 조정을 위한 2진 자리2
  pinMode(DIP3, INPUT);//점등 시간 조정을 위한 2진 자리3
  pinMode(DIP4, INPUT);//점등 시간 조정을 위한 2진 자리4

  pinMode(SW1, INPUT);
  pinMode(SW2, INPUT);
  pinMode(SW3, INPUT);
  pinMode(SW4, INPUT);
}

void loop() {
  while(true){
    //int Order = LIGHT_TIME(digitalRead(DIP4), digitalRead(DIP3), digitalRead(DIP2), digitalRead(DIP1));
    
    for(int i=0; i<255; i++){
      analogWrite(PWM1, i);
      Serial.println(digitalRead(SW1));
      if (digitalRead(SW1)==1);{
        break
        };
      delay(10);   
      }
    for(int i=255; i>0; i--){
      analogWrite(PWM1, i);
      Serial.println(digitalRead(SW1));
      if (digitalRead(SW1)==1);{
        break
        };
      }
      delay(10);
      }
    delay(1000);
    }
}

int LIGHT_TIME(int pin4, int pin3, int pin2, int pin1){
  if (pin4==0 && pin3==0 && pin2==0 && pin1==0){
    int T=0;
    }
  if (pin4==0 && pin3==0 && pin2==0 && pin1==1){
    int T=1;
    }
  if (pin4==0 && pin3==0 && pin2==1 && pin1==0){
    int T=2;
    }
  if (pin4==0 && pin3==0 && pin2==1 && pin1==1){
    int T=3;
    }
  if (pin4==0 && pin3==1 && pin2==0 && pin1==0){
    int T=4;
    }
  if (pin4==0 && pin3==1 && pin2==0 && pin1==1){
    int T=5;
  }
  if (pin4==0 && pin3==1 && pin2==1 && pin1==0){
    int T=6;
    }
  if (pin4==0 && pin3==1 && pin2==1 && pin1==1){
    int T=7;
    }
  if (pin4==1 && pin3==0 && pin2==0 && pin1==0){
    int T=8;
    }
  if (pin4==1 && pin3==0 && pin2==0 && pin1==1){
    int T=9;
    }
  if (pin4==1 && pin3==0 && pin2==1 && pin1==0){
    int T=10;
    }
  if (pin4==1 && pin3==0 && pin2==1 && pin1==1){
    int T=11;
    }
  if (pin4==1 && pin3==1 && pin2==0 && pin1==0){
    int T=12;
    }
  if (pin4==1 && pin3==1 && pin2==0 && pin1==1){
    int T=13;
    }
  if (pin4==1 && pin3==1 && pin2==1 && pin1==0){
    int T=14;
    }
  if (pin4==1 && pin3==1 && pin2==1 && pin1==1){
    int T=15;
    }
  return (T);
  }
