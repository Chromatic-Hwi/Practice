int interruptChecker = A15;
int RunOrStop;

char digitalInA1 = A0;
char digitalInA2 = A1;
char digitalInA3 = A2;
char digitalInB1 = A8;
char digitalInB2 = A9;
char digitalInB3 = A10;

int inputValueA1;
int inputValueA2;
int inputValueA3;
int inputValueB1;
int inputValueB2;
int inputValueB3;
/*
char HiLowA1 = "L";
char HiLowA2 = "L";
char HiLowA3 = "L";
char HiLowB1 = "L";
char HiLowB2 = "L";
char HiLowB3 = "L";
*/

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
  
  /*
  char SentenceValue[70];
  sprintf(Sentence , "OutputA : {%2d, %2d, %2d}  |  OutPutB : {%2d, %2d, %2d}", 
  inputValueA1, inputValueA2, inputValueA3,
  inputValueB1, inputValueB2, inputValueB3);
  */
  /*
  char SentenceBool[70];
  if (inputValueA1>100){HiLowA1 = "H";}
  else {HiLowA1 = "L";}
  if (inputValueA2>100){HiLowA2 = "H";}
  else {HiLowA2 = "L";}
  if (inputValueA3>100){HiLowA3 = "H";}
  else {HiLowA3 = "L";}

  if (inputValueB1>100){HiLowB1 = "H";}
  else {HiLowB1 = "L";}
  if (inputValueB2>100){HiLowB2 = "H";}
  else {HiLowB2 = "L";}
  if (inputValueB3>100){HiLowB3 = "H";}
  else {HiLowB3 = "L";}
  
  sprintf(SentenceBool , "OutputA : {%s, %s, %s}  |  OutPutB : {%s, %s, %s}", 
  HiLowA1, HiLowA2, HiLowA3,
  HiLowB1, HiLowB2, HiLowB3);
  */
  
  if (RunOrStop != 0){
    //Serial.println(SentenceValue);
    //Serial.println(SentenceBool);
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
    Serial.println("[No print mode], Remove Gnd from A0 to restart print.");
    delay(5000);
    }
  //
  
}
