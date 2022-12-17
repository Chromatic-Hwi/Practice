'''
주석 설명은 삭제의 편의를 위해 동작 위에 기입.
링크도 같이 첨부했으니 참고할 것.
Flask 연결 부분은 대강적인 흐름만 유추해서 적어놨음.
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 시간 측정+기록이나 동작 지연을 위한 모듈
import time

# 플라스크 임포트
from flask import Flask
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 플라스크 동작 실행

# 버튼으로 입력된 값이 High/Low 인지 아니면 True/False인지 1/0인지 확인하고 입력.

Button0 = Flask~~~~(코드들)
Button1 = Flask~~~~(코드들)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 라즈베리(=RPi) GPIO 컨트롤 모듈
impot RPi.GPIO as GPIO 

# GPIO의 동작을 결정하는 setmode는 RPi 보드의 포트 순서를 기준으로 하는 BOARD와 포트 역할을 기준으로 하는 BCM 모드가 있다.
# 그냥 꽂는건 순서대로 꽂으면 되니 BOARD 모드가 편리하지만, 전원 포트를 구분하고 포트들의 성격을 구분해 사용하기 위해 나는 BCM을 선호하는 편.
# https://m.blog.naver.com/pk3152/221368513358
GPIO.setmode(GPIO.BCM)

# 23, 24, 27, 16, 20, 21...은 PWM이나 SP10 등의 특별한 역할이 아닌 단순 연결 포트

# GPIO23과 GPIO24를 저항 풀다운(-> 모르면 찾아서 공부) 입력으로 설정.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO20, GPIO21을 출력으로 설정.
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

Input0 = GPIO.input(23)
Input1 = GPIO.input(24)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# try문으로 예외 에러를 처리하고 동작 인터럽트를 추가.
try:
    while True:
        NowTime = time.strftime('%y/%m/%d - %H:%M:%S')
        print(NowTime)
        print()

        print("Input0 Value >>", Input0, " | ", "Input1 Value >>", Input1, "\n")

        # 밑에 if문 한줄은 플라스크 버튼 입력에 따라 동작을 컨트롤하는 예시
        #if (Button0==False & Button1==False):
        
        # GPIO 입력에 따라 출력 핀에 연결된 모듈을 키고 끄는 경우들
        if (Input0==False & Input0==False):
            GPIO.output(20, False)
            GPIO.output(21, False)

        elif (Input0==True & Input0==False):
            GPIO.output(20, True)
            GPIO.output(21, False)

        elif (Input0==False & Input0==True):
            GPIO.output(20, False)
            GPIO.output(21, True)

        elif (Input0==True & Input0==True):
            GPIO.output(20, True)
            GPIO.output(21, True)

        time.sleep(1.0)

# Ctrl+ C 키를 누르면 전체 동작에 끼어드는 인터럽트 발생 -> 미리 인터럽트 경우를 만들어서 동작 중지 명령
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    time.sleep(0.5)

except:
    print("Wrong Key! Error!")

# try든 except든 최종적으로(FInally) 이 부분에 도착, 실행
# GPIO에 설정된 값들은 파이썬 프로그램이 종료되도 초기화되지 않기 때문에 사용자가 값을 지워줘야 함. Clean UP!
finally:
    print("Clean Up")
    GPIO.cleanup()

        

        
