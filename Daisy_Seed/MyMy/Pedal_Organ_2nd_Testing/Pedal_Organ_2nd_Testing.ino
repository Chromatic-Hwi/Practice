//#include <Tone.h>

int output = 13;

// 입력 지정     (C, C#, D, D#, E, F, F#, G, G#, A, A#, B 총 12개)
int input[12] = {1, 2,  3, 4,  5, 6, 7,  8, 9, 10, 11, 12};

// 기본 주파수는 E2를 기준으로 해서 +-1 옥타브 한다.
// 2로 나누거나 곱하는데 연산 시간이 소요되므로 레이턴시를 최소화하기 위해서 미리 주파수를 다 정해놓는게 나을듯함.
//int freqE1[12] = {32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74};
int freqE2[12] = {65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5};

int chk = 0;

void setup() {
  pinMode(output, OUTPUT);
  
  for (int idx=0; idx<11; idx++) {
    pinMode(input[idx], INPUT);
  }
}

void loop() {
  tone(output, freqE2[0]*2);
  delay(500);
  tone(output, freqE2[4]*2);
  delay(500);
  tone(output, freqE2[7]*2);
  delay(500);
  /*
  for (int idx=0; idx<11; idx++) {
    chk = digitalRead(input[idx]);
    
    // 스위치 눌림 체크 후 눌림이 멈추면 소리 출력 중단
    if (chk) {
      tone(output, freqE2[idx]);
      while (digitalRead(input[idx]));
      noTone(output);
    }
  }
  */
}
