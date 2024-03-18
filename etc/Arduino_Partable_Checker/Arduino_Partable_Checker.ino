char interruptChecker = A0;
int RunOrStop;

char digitalInA1 = A1;
char digitalInA2 = A2;
char digitalInA3 = A3;
char digitalInB1 = A5;
char digitalInB2 = A6;
char digitalInB3 = A7;

int digitalOutA1 = 23;
int digitalOutA2 = 25;
int digitalOutA3 = 27;
int digitalOutA4 = 29;
int digitalOutA5 = 31;
int digitalOutA6 = 33;

int digitalOutB1 = 22;
int digitalOutB2 = 24;
int digitalOutB3 = 26;
int digitalOutB4 = 28;
int digitalOutB5 = 30;
int digitalOutB6 = 32;


int inputValueA1;
int inputValueA2;
int inputValueA3;
int inputValueB1;
int inputValueB2;
int inputValueB3;

void setup(void)
{
    Serial.begin(9600);
    pinMode(interruptChecker, INPUT);
    
    pinMode(digitalInA1, INPUT);
    pinMode(digitalInA2, INPUT);
    pinMode(digitalInA3, INPUT);
    pinMode(digitalInB1, INPUT);
    pinMode(digitalInB2, INPUT);
    pinMode(digitalInB3, INPUT);
    
    pinMode(digitalOutA1, OUTPUT);
    pinMode(digitalOutA2, OUTPUT);
    pinMode(digitalOutA3, OUTPUT);
    pinMode(digitalOutA4, OUTPUT);
    pinMode(digitalOutA5, OUTPUT);
    pinMode(digitalOutA6, OUTPUT);
    
    pinMode(digitalOutB1, OUTPUT);
    pinMode(digitalOutB2, OUTPUT);
    pinMode(digitalOutB3, OUTPUT);
    pinMode(digitalOutB4, OUTPUT);
    pinMode(digitalOutB5, OUTPUT);
    pinMode(digitalOutB6, OUTPUT);
    
}
 
void loop(void)
{
  RunOrStop = analogRead(interruptChecker);

  inputValueA1 = digitalRead(digitalInA1);
  inputValueA2 = digitalRead(digitalInA2);
  inputValueA3 = digitalRead(digitalInA3);
  inputValueB1 = digitalRead(digitalInB1);
  inputValueB2 = digitalRead(digitalInB2);
  inputValueB3 = digitalRead(digitalInB3);
  
  digitalWrite(digitalOutA1, HIGH);
  digitalWrite(digitalOutA2, HIGH);
  digitalWrite(digitalOutA3, HIGH);
  digitalWrite(digitalOutA4, HIGH);
  digitalWrite(digitalOutA5, HIGH);
  digitalWrite(digitalOutA6, HIGH);
  digitalWrite(digitalOutB1, LOW);
  digitalWrite(digitalOutB2, LOW);
  digitalWrite(digitalOutB3, LOW);
  digitalWrite(digitalOutB4, LOW);
  digitalWrite(digitalOutB5, LOW);
  digitalWrite(digitalOutB6, LOW);
  
  if (RunOrStop != 0){
    Serial.print("OutputA : {");
    Serial.print(inputValueA1);
    Serial.print(", ");
    Serial.print(inputValueA2);
    Serial.print(", ");
    Serial.print(inputValueA3);
    Serial.print("}  |  ");
    
    Serial.print("OutputB : {");
    Serial.print(inputValueB1);
    Serial.print(", ");
    Serial.print(inputValueB2);
    Serial.print(", ");
    Serial.print(inputValueB3);
    Serial.println("}");
    
    delay(200);
    }
    
  else{
    Serial.println("[No print mode], Remove Gnd from A0 to print.");
    delay(5000);
    }
  //
  
}
