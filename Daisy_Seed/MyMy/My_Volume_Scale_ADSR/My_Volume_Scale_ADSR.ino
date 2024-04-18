#include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

static AdEnv adenv;
static Oscillator osc;

float pitch;
float analog_knob;
float volume;

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
    button_pressed = adenv.Process();
    
    osc.SetFreq(pitch);
    osc.SetAmp(volume);
  
    out_signal = osc.Process();
    out[0][i] = out_signal; 
    out[1][i] = out_signal; 
  }
}



void setup() {
  float sample_rate;
  // Initialize seed at 48kHz
  hw = DAISY.init(DAISY_SEED, AUDIO_SR_48K);
  num_channels = hw.num_channels;
  sample_rate = DAISY.get_samplerate();
  
  osc.Init(sample_rate);
  // Set the parameters for oscillator 
  osc.SetWaveform(osc.WAVE_SQUARE); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc.SetFreq(440);
  osc.SetAmp(0.5);
  
  // Set the value of Env
  // Atack, Decay, Sustain, Release => ADSR
  adenv.Init(sample_rate);
  adenv.SetTime(ADENV_SEG_ATTACK, 0.05);
  adenv.SetTime(ADENV_SEG_DECAY, 0.05);
  adenv.SetMin(0);
  adenv.SetMax(0);
  adenv.SetCurve(0);
  
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
  
  if (buttonC.Pressed()){
    pitch = freqE2[0] * 2;
    button_pressed = buttonC.Pressed();
    }
  else if (buttonD.Pressed()){
    pitch = freqE2[2] * 2;
    button_pressed = buttonD.Pressed();
    }
  else if (buttonE.Pressed()){
    pitch = freqE2[4] * 2;
    button_pressed = buttonE.Pressed();
    }
  else if (buttonF.Pressed()){
    pitch = freqE2[5] * 2;
    button_pressed = buttonF.Pressed();
    }
  else if (buttonG.Pressed()){
    pitch = freqE2[7] * 2;
    button_pressed = buttonG.Pressed();
    }
  else if (buttonA.Pressed()){
    pitch = freqE2[9] * 2;
    button_pressed = buttonA.Pressed();
    }
  else if (buttonB.Pressed()){
    pitch = freqE2[11] * 2;
    button_pressed = buttonB.Pressed();
    }
  // amp_button ==>> 눌렀을 때 1
  volume = analog_knob / 65535.0 * button_pressed;
  
  delay(1);
  }
