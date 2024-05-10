 #include "DaisyDuino.h"

DaisyHardware hw;
size_t num_channels;

static AdEnv adenv;
static Oscillator osc_C;
static Oscillator osc_CC;
static Oscillator osc_D;
static Oscillator osc_DD;
static Oscillator osc_E;
static Oscillator osc_F;
static Oscillator osc_FF;
static Oscillator osc_G;
static Oscillator osc_GG;
static Oscillator osc_A;
static Oscillator osc_AA;
static Oscillator osc_B;
float osc_Sum;

// From Autowah
static Metro tick;
static Autowah autowah;

float env_on;

float oct = 2; // 1=E2, 2=E3

float analog_input0;
float analog_input1;
float analog_input2;
float analog_input3;
float analog_input4;

float analog_value0;
float analog_value1;
float analog_value2;
float analog_value3;
float analog_value4;

float volume_C;
float volume_CC;
float volume_D;
float volume_DD;
float volume_E;
float volume_F;
float volume_FF;
float volume_G;
float volume_GG;
float volume_A;
float volume_AA;
float volume_B;

Switch buttonC;
Switch buttonCC;
Switch buttonD;
Switch buttonDD;
Switch buttonE;
Switch buttonF;
Switch buttonFF;
Switch buttonG;
Switch buttonGG;
Switch buttonA;
Switch buttonAA;
Switch buttonB;

float freqE2[12] = {65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5};

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void MyCallback(float **in, float **out, size_t size) 
{
  float out_signal;
  
  buttonC.Debounce();
  buttonCC.Debounce();
  buttonD.Debounce();
  buttonDD.Debounce();
  buttonE.Debounce();
  buttonF.Debounce();
  buttonFF.Debounce();
  buttonG.Debounce();
  buttonGG.Debounce();
  buttonA.Debounce();
  buttonAA.Debounce();
  buttonB.Debounce();

  /*
  // Don't delete / Sustain과 Env를 버튼 클릭에만 한정하도록 함.
  // If press the button Trigger ON
  if(buttonC.RisingEdge()){adenv.Trigger();}
  else if(buttonCC.RisingEdge()){adenv.Trigger();}
  else if(buttonD.RisingEdge()){adenv.Trigger();}
  else if(buttonDD.RisingEdge()){adenv.Trigger();}
  else if(buttonE.RisingEdge()){adenv.Trigger();}
  else if(buttonF.RisingEdge()){adenv.Trigger();}
  else if(buttonFF.RisingEdge()){adenv.Trigger();}
  else if(buttonG.RisingEdge()){adenv.Trigger();}
  else if(buttonGG.RisingEdge()){adenv.Trigger();}
  else if(buttonA.RisingEdge()){adenv.Trigger();}
  else if(buttonAA.RisingEdge()){adenv.Trigger();}
  else if(buttonB.RisingEdge()){adenv.Trigger();}
  */
  
  for (size_t i = 0; i < size; i++) {
    // When the metro ticks, trigger the envelope to start.
    if (tick.Process()){
      adenv.Trigger();
      }
      
    env_on = adenv.Process();
    
    osc_C.SetFreq(freqE2[0] * oct);
    osc_C.SetAmp(volume_C*env_on);

    osc_CC.SetFreq(freqE2[1] * oct);
    osc_CC.SetAmp(volume_CC*env_on);
    
    osc_D.SetFreq(freqE2[2] * oct);
    osc_D.SetAmp(volume_D*env_on);

    osc_DD.SetFreq(freqE2[3] * oct);
    osc_DD.SetAmp(volume_DD*env_on);
    
    osc_E.SetFreq(freqE2[4] * oct);
    osc_E.SetAmp(volume_E*env_on);

    osc_F.SetFreq(freqE2[5] * oct);
    osc_F.SetAmp(volume_F*env_on);

    osc_FF.SetFreq(freqE2[6] * oct);
    osc_FF.SetAmp(volume_FF*env_on);
    
    osc_G.SetFreq(freqE2[7] * oct);
    osc_G.SetAmp(volume_G*env_on);

    osc_GG.SetFreq(freqE2[8] * oct);
    osc_GG.SetAmp(volume_GG*env_on);

    osc_A.SetFreq(freqE2[9] * oct);
    osc_A.SetAmp(volume_A*env_on);

    osc_AA.SetFreq(freqE2[10] * oct);
    osc_AA.SetAmp(volume_AA*env_on);
    
    osc_B.SetFreq(freqE2[11] * oct);
    osc_B.SetAmp(volume_B*env_on);
    
    out[0][i] = osc_C.Process() + osc_CC.Process() + osc_D.Process() + osc_DD.Process() + osc_E.Process() + osc_F.Process() + osc_FF.Process() + osc_G.Process() + osc_GG.Process() + osc_A.Process() + osc_AA.Process() + osc_B.Process();
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
  osc_C.Init(sample_rate);
  osc_C.SetWaveform(osc_C.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_C.SetFreq(440);
  osc_C.SetAmp(0.5);

  osc_CC.Init(sample_rate);
  osc_CC.SetWaveform(osc_CC.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_CC.SetFreq(440);
  osc_CC.SetAmp(0.5);

  osc_D.Init(sample_rate);
  osc_D.SetWaveform(osc_D.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_D.SetFreq(440);
  osc_D.SetAmp(0.5);

  osc_DD.Init(sample_rate);
  osc_DD.SetWaveform(osc_DD.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_DD.SetFreq(440);
  osc_DD.SetAmp(0.5);
  
  osc_E.Init(sample_rate);
  osc_E.SetWaveform(osc_E.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_E.SetFreq(440);
  osc_E.SetAmp(0.5);

  osc_F.Init(sample_rate);
  osc_F.SetWaveform(osc_F.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_F.SetFreq(440);
  osc_F.SetAmp(0.5);

  osc_FF.Init(sample_rate);
  osc_FF.SetWaveform(osc_FF.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_FF.SetFreq(440);
  osc_FF.SetAmp(0.5);

  osc_G.Init(sample_rate);
  osc_G.SetWaveform(osc_G.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_G.SetFreq(440);
  osc_G.SetAmp(0.5);

  osc_GG.Init(sample_rate);
  osc_GG.SetWaveform(osc_GG.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_GG.SetFreq(440);
  osc_GG.SetAmp(0.5);

  osc_A.Init(sample_rate);
  osc_A.SetWaveform(osc_A.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_A.SetFreq(440);
  osc_A.SetAmp(0.5);

  osc_AA.Init(sample_rate);
  osc_AA.SetWaveform(osc_AA.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_AA.SetFreq(440);
  osc_AA.SetAmp(0.5);

  osc_B.Init(sample_rate);
  osc_B.SetWaveform(osc_B.WAVE_TRI); // WAVE_SIN, WAVE_SQUARE, WAVE_TRI
  osc_B.SetFreq(440);
  osc_B.SetAmp(0.5);
  
  // Set the value of Env
  // Atack, Decay, Sustain, Release => ADSR
  adenv.Init(sample_rate);
  adenv.SetTime(ADENV_SEG_ATTACK, 0.02f);
  adenv.SetTime(ADENV_SEG_DECAY, 0.35f);
  adenv.SetMin(0.f); // 0으로 하면  env 싸이클 종료후 음 출력 안됨.
  adenv.SetMax(1.f);
  adenv.SetCurve(1);

  // Set up metro to pulse every second
  tick.Init(3.0f, sample_rate); // 1~10 사이를 컨트롤 하도록 pot

  // set autowah parameters
  autowah.Init(sample_rate);
  autowah.SetLevel(.1);
  autowah.SetDryWet(100);
  autowah.SetWah(1); //20까지 올려봤는데 차이 체감 X
  
  // Check value of pot
  Serial.begin(9600);

  // button Init
  buttonC.Init(1000, true, 0, INPUT_PULLUP);
  buttonCC.Init(1000, true, 1, INPUT_PULLUP);
  buttonD.Init(1000, true, 2, INPUT_PULLUP);
  buttonDD.Init(1000, true, 3, INPUT_PULLUP);
  buttonE.Init(1000, true, 4, INPUT_PULLUP);
  buttonF.Init(1000, true, 5, INPUT_PULLUP);
  buttonFF.Init(1000, true, 6, INPUT_PULLUP);
  buttonG.Init(1000, true, 7, INPUT_PULLUP);
  buttonGG.Init(1000, true, 8, INPUT_PULLUP);
  buttonA.Init(1000, true, 9, INPUT_PULLUP);
  buttonAA.Init(1000, true, 10, INPUT_PULLUP);
  buttonB.Init(1000, true, 11, INPUT_PULLUP);
  
  DAISY.begin(MyCallback);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  analogReadResolution(16); //Not a GPIO Num

  analog_input0 = analogRead(A0); //0~65535
  analog_input1 = analogRead(A1);
  analog_input2 = analogRead(A2);
  analog_input3 = analogRead(A3);
  analog_input4 = analogRead(A4);
  
  analog_value0 = analog_input0 / 655.35;
  analog_value1 = analog_input1 / 655.35;
  analog_value2 = analog_input2 / 655.35;
  analog_value3 = analog_input3 / 655.35;
  analog_value4 = analog_input4 / 6553.5;
  
  // amp_button ==>> 눌렀을 때 1
  volume_C = analog_value0  * buttonC.Pressed();
  volume_CC = analog_value0 * buttonCC.Pressed();
  volume_D = analog_value0 * buttonD.Pressed();
  volume_DD = analog_value0 * buttonDD.Pressed();
  volume_E = analog_value0 * buttonE.Pressed();
  volume_F = analog_value0 * buttonF.Pressed();
  volume_FF = analog_value0 * buttonFF.Pressed();
  volume_G = analog_value0 * buttonG.Pressed();
  volume_GG = analog_value0 * buttonGG.Pressed();
  volume_A = analog_value0 * buttonA.Pressed();
  volume_AA = analog_value0 * buttonAA.Pressed();
  volume_B = analog_value0 * buttonB.Pressed();

  Serial.print(analog_value0);
  Serial.print("  |  ");
  Serial.print(analog_value1);
  Serial.print("  |  ");
  Serial.print(analog_value2);
  Serial.print("  |  ");
  Serial.print(analog_value3);
  Serial.print("  |  ");
  Serial.println(analog_value4);
  delay(100);
  }
