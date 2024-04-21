#include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

static AdEnv adenv;
static Oscillator osc_C;
static Oscillator osc_D;
static Oscillator osc_E;
static Oscillator osc_F;
static Oscillator osc_G;
static Oscillator osc_A;
static Oscillator osc_B;

float oct = 2; // 1=E2, 2=E3
float analog_knob;
float env_on;

float volume_C;
float volume_D;
float volume_E;
float volume_F;
float volume_G;
float volume_A;
float volume_B;

Switch buttonC;
Switch buttonD;
Switch buttonE;
Switch buttonF;
Switch buttonG;
Switch buttonA;
Switch buttonB;

float button_pressed;

float freqE2[12] = {65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5};


void MyCallback(float **in, float **out, size_t size) 
{
  float out_signal;
  
  buttonC.Debounce();
  buttonD.Debounce();
  buttonE.Debounce();
  buttonF.Debounce();
  buttonG.Debounce();
  buttonA.Debounce();
  buttonB.Debounce();
  
  // If press the button
  if(buttonC.RisingEdge()){adenv.Trigger();}
  else if(buttonD.RisingEdge()){adenv.Trigger();}
  else if(buttonE.RisingEdge()){adenv.Trigger();}
  else if(buttonF.RisingEdge()){adenv.Trigger();}
  else if(buttonG.RisingEdge()){adenv.Trigger();}
  else if(buttonA.RisingEdge()){adenv.Trigger();}
  else if(buttonB.RisingEdge()){adenv.Trigger();}
  
  for (size_t i = 0; i < size; i++) {
    // Process the envelope (env 효과를 최소로 하면 env가 끝남과 동시에 서스테인도 끝나게 하는 효과)
    env_on = adenv.Process();

    osc_C.SetFreq(freqE2[0] * oct);
    osc_C.SetAmp(volume_C*env_on);

    osc_D.SetFreq(freqE2[2] * oct);
    osc_D.SetAmp(volume_D*env_on);
    
    osc_E.SetFreq(freqE2[4] * oct);
    osc_E.SetAmp(volume_E*env_on);

    osc_F.SetFreq(freqE2[5] * oct);
    osc_F.SetAmp(volume_F*env_on);
    
    osc_G.SetFreq(freqE2[7] * oct);
    osc_G.SetAmp(volume_G*env_on);

    osc_A.SetFreq(freqE2[9] * oct);
    osc_A.SetAmp(volume_A*env_on);
    
    osc_B.SetFreq(freqE2[11] * oct);
    osc_B.SetAmp(volume_B*env_on);
    
    out[0][i] = osc_C.Process() + osc_D.Process() + osc_E.Process() + osc_F.Process() + osc_G.Process() + osc_A.Process() + osc_B.Process();
    out[1][i] = out_signal; 
  }
}



void setup() {
  float sample_rate;
  // Initialize seed at 48kHz
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();
  
  osc_C.Init(sample_rate);
  // Set the parameters for oscillator 
  osc_C.SetWaveform(osc_C.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_C.SetFreq(440);
  osc_C.SetAmp(0.2);

  osc_D.Init(sample_rate);
  osc_D.SetWaveform(osc_D.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_D.SetFreq(440);
  osc_D.SetAmp(0.2);
  
  osc_E.Init(sample_rate);
  osc_E.SetWaveform(osc_E.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_E.SetFreq(440);
  osc_E.SetAmp(0.2);

  osc_F.Init(sample_rate);
  osc_F.SetWaveform(osc_F.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_F.SetFreq(440);
  osc_F.SetAmp(0.2);

  osc_G.Init(sample_rate);
  osc_G.SetWaveform(osc_G.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_G.SetFreq(440);
  osc_G.SetAmp(0.2);

  osc_A.Init(sample_rate);
  osc_A.SetWaveform(osc_A.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_A.SetFreq(440);
  osc_A.SetAmp(0.2);

  osc_B.Init(sample_rate);
  osc_B.SetWaveform(osc_B.WAVE_SIN); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_B.SetFreq(440);
  osc_B.SetAmp(0.2);
  
  // Set the value of Env
  // Atack, Decay, Sustain, Release => ADSR
  adenv.Init(sample_rate);
  adenv.SetTime(ADENV_SEG_ATTACK, 0.01);
  adenv.SetTime(ADENV_SEG_DECAY, 0.35);
  adenv.SetMin(0); // 0으로 하면  env 싸이클 종료후 음 출력 안됨.
  adenv.SetMax(10);
  adenv.SetCurve(1);
  
  // Check value of pot
  Serial.begin(9600);

  // button Init
  buttonC.Init(1000, true, 16, INPUT_PULLUP);
  buttonD.Init(1000, true, 17, INPUT_PULLUP);
  buttonE.Init(1000, true, 18, INPUT_PULLUP);
  buttonF.Init(1000, true, 19, INPUT_PULLUP);
  buttonG.Init(1000, true, 20, INPUT_PULLUP);
  buttonA.Init(1000, true, 21, INPUT_PULLUP);
  buttonB.Init(1000, true, 22, INPUT_PULLUP);
  
  DAISY.begin(MyCallback);
}



void loop() {
  analogReadResolution(16); //Not a GPIO Num

  analog_knob = analogRead(A0);
  //Serial.println(analogRead(A0)); //300~65535
  
  if (buttonC.Pressed()){button_pressed = buttonC.Pressed();}
  else if (buttonD.Pressed()){button_pressed = buttonD.Pressed();}
  else if (buttonE.Pressed()){button_pressed = buttonE.Pressed();}
  else if (buttonF.Pressed()){button_pressed = buttonF.Pressed();}
  else if (buttonG.Pressed()){button_pressed = buttonG.Pressed();}
  else if (buttonA.Pressed()){button_pressed = buttonA.Pressed();}
  else if (buttonB.Pressed()){button_pressed = buttonB.Pressed();}
  // amp_button ==>> 눌렀을 때 1
  //volume = analog_knob / 65535.0 * button_pressed;
  volume_C = analog_knob / 65535.0 * buttonC.Pressed();
  volume_D = analog_knob / 65535.0 * buttonD.Pressed();
  volume_E = analog_knob / 65535.0 * buttonE.Pressed();
  volume_F = analog_knob / 65535.0 * buttonF.Pressed();
  volume_G = analog_knob / 65535.0 * buttonG.Pressed();
  volume_A = analog_knob / 65535.0 * buttonA.Pressed();
  volume_B = analog_knob / 65535.0 * buttonB.Pressed();
  
  delay(10);
  }
