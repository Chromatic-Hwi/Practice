#include "DaisyDuino.h"

DaisyHardware hw;
static Oscillator osc;
float pitch_knob;
float amp_knob;

Switch button;
float amp_button;

size_t num_channels;

void MyCallback(float **in, float **out, size_t size) {
  float sine_signal;
  button.Debounce();
  
  osc.SetFreq(pitch_knob);
  osc.SetAmp(amp_knob * amp_button);
  
  for (size_t i = 0; i < size; i++) {
    sine_signal = osc.Process();
    out[0][i] = sine_signal; 
    out[1][i] = sine_signal; 
  }
}

void setup() {
  // Initialize seed at 48kHz
  float sample_rate;
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();
  osc.Init(sample_rate);

  // Set the parameters for oscillator 
  osc.SetWaveform(osc.WAVE_SIN);
  osc.SetFreq(100);
  osc.SetAmp(0.5);
  
  // Check value of pot
  Serial.begin(9600);

  // button Init
  button.Init(1000, true, 26, INPUT_PULLUP);
  
  DAISY.begin(MyCallback);
}

void loop() {
  analogReadResolution(16);
  pitch_knob = (220.0 * (analogRead(A0) / 65535.0)) + 220.0;
  amp_knob = analogRead(A1) / 65535.0;

  amp_button = button.Pressed();

  Serial.println(analogRead(A0));
  delay(1);
  }
