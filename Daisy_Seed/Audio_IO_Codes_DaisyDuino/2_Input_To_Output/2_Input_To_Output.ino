#include "DaisyDuino.h"

DaisyHardware hw;
static Oscillator osc;

size_t num_channels;

void MyCallback(float **in, float **out, size_t size) {
  float sine_signal;
  for (size_t i = 0; i < size; i++) {
    sine_signal = osc.Process();
    out[0][i] = in[0][i]; //sine_signal;
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
  osc.SetFreq(440);
  osc.SetAmp(0.5);

  // start callback
  DAISY.begin(MyCallback);
}

void loop() {}
