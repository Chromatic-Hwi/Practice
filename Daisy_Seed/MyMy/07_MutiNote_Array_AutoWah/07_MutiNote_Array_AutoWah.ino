#include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

static AdEnv adenv;
static Oscillator osc[12];
float osc_Sum;

// From Autowah
static Metro tick;
static Autowah autowah;

float oct = 2; // 1=E2, 2=E3
float analog_knob;
float env_on;

float volume[12];

Switch button[12];

float button_pressed;

float freqE2[12] = {65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5};

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void MyCallback(float **in, float **out, size_t size) 
{
  float out_signal;

  for (int i = 0; i<12; i++){
    button[i].Debounce();
    }
  
  // If press the button Trigger ON
  for (int i = 0; i<12; i++){
    if (button[i].RisingEdge()){
      adenv.Trigger();
      break;
      }
    }
  
  for (size_t i = 0; i < size; i++) {
    // When the metro ticks, trigger the envelope to start.
    if (tick.Process()) {
      adenv.Trigger();
    }
    
    env_on = adenv.Process();

    for (int i = 0; i<12; i++){
    osc[i].SetFreq(freqE2[i] * oct);
    osc[i].SetAmp(volume[i]*env_on);
    }
    
    out[0][i] = osc[0].Process() + osc[2].Process() + osc[4].Process() + osc[5].Process() + osc[7].Process() + osc[9].Process() + osc[11].Process();
    //out[1][i] = out_signal; 
  }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
  float sample_rate;
  // Initialize seed at 48kHz
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();

  // Set the parameters for oscillator 
  for (int i = 0; i<12; i++){
    osc[i].Init(sample_rate);
    osc[i].SetWaveform(osc[i].WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
    osc[i].SetFreq(440);
    osc[i].SetAmp(0.5);
    }
  
  // Set the value of Env
  // Atack, Decay, Sustain, Release => ADSR
  adenv.Init(sample_rate);
  adenv.SetTime(ADENV_SEG_ATTACK, 0.02f);
  adenv.SetTime(ADENV_SEG_DECAY, 0.35f);
  adenv.SetMin(0.f); // 0으로 하면  env 싸이클 종료후 음 출력 안됨.
  adenv.SetMax(5.f);
  adenv.SetCurve(1);  //

  // Set up metro to pulse every second
  tick.Init(3.0f, sample_rate); // 1~10 사이를 컨트롤 하도록 pot
  
  // set autowah parameters
  autowah.Init(sample_rate);
  autowah.SetLevel(.1);
  autowah.SetDryWet(100);
  autowah.SetWah(1);
  
  // Check value of pot
  Serial.begin(9600);

  // button Init
  for (int i = 0; i<12; i++){
    button[i].Init(1000, true, 16, INPUT_PULLUP);
    }
  
  DAISY.begin(MyCallback);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  analogReadResolution(16); //Not a GPIO Num

  analog_knob = analogRead(A0);
  //Serial.println(analogRead(A0)); //300~65535
  
  // amp_button ==>> 눌렀을 때 1
  for (int i = 0; i<12; i++){
    button[i].Init(1000, true, 16, INPUT_PULLUP);
    volume[i] = analog_knob / 65535.0 * button[i].Pressed();
    }
  
  delay(1);
  }
