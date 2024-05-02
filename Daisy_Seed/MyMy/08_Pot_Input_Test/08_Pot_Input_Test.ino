 #include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

float analog_value0;
float analog_value1;
float analog_value2;
float analog_value3;
float analog_value4;

float analog_knob0;
float analog_knob1;
float analog_knob2;
float analog_knob3;
float analog_knob4;

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  float sample_rate;
  // Initialize seed at 48kHz
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();
  
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  
  // Check value of pot
  Serial.begin(9600);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  analogReadResolution(16); //Not a GPIO Num

  analog_value0 = analogRead(A0);
  analog_value1 = analogRead(A1);
  analog_value2 = analogRead(A2);
  analog_value3 = analogRead(A3);
  analog_value4 = analogRead(A4);
  //Serial.println(analogRead(A0)); //300~65535

  Serial.print(analog_value0);
  Serial.print("  |  ");
  Serial.print(analog_value1);
  Serial.print("  |  ");
  Serial.print(analog_value2); 
  Serial.print("  |  ");
  Serial.println(analog_value3);
  delay(100);
  }
