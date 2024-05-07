 #include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

float analog_value0;
float analog_value1;
float analog_value2;
float analog_value3;

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  float sample_rate;
  // Initialize seed at 48kHz
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();

  // Check value of pot
  Serial.begin(9600);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  analogReadResolution(16); //Not a GPIO Num

  analog_value0 = analogRead(A0); //0~65535
  analog_value1 = analogRead(A1);
  analog_value2 = analogRead(A2);
  analog_value3 = analogRead(A3);

  Serial.print(analog_value0);
  Serial.print("  |  ");
  Serial.print(analog_value1);
  Serial.print("  |  ");
  Serial.print(analog_value2); 
  Serial.print("  |  ");
  Serial.println(analog_value3);
  delay(100);
  }
