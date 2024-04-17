#include "DaisyDuino.h"

DaisyHardware hw;
static Oscillator osc;
float pitch_knob;
size_t num_channels;

void MyCallback(float **in, float **out, size_t size) {
  float sine_signal;
  osc.SetFreq(pitch_knob);
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
  osc.SetWaveform(osc.WAVE_SAW);
  osc.SetFreq(440);
  osc.SetAmp(0.5);

  // start callback
  DAISY.begin(MyCallback);
}

void loop() {
  analogReadResolution(16);
  pitch_knob = (analogRead(A0) / 65535.0 * 440.0) + 440.0;
  
  }
