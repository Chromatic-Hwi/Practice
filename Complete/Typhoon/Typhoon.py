from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
#============================================================================================
from datetime import datetime as DT
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#============================================================================================
f = open('./Mail_info.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

meID=info[1]
mePW=info[3]
#============================================================================================
def WIND_FORCE(spd):
    if spd<1:
        return ["Calm", "연기가 외부 영향없이 수직으로 올라가는 상태"]
    if spd>=1 and spd<=5:
        return ["Light air", "풍향계는 움직이지 않지만 풍향만 겨우 알 수 있는 상태"]
    elif spd>=6 and spd<=11:
        return ["Light breeze", "나뭇잎이 흔들리고 풍향계가 움직이기 시작하는 상태"]
    elif spd>=12 and spd<=19:
        return ["Fresh breeze", "나뭇잎과 가는 가지가 계속 흔들리고 깃발이 가볍게 날리는 상태"]
    elif spd>=20 and spd<=28:
        return ["Moderate breeze", "먼지가 일고 작은 가지가 흔들리는 상태"]
    elif spd>=29 and spd<=38:
        return ["Fresh breeze", "잎이 무성한 나무가 흔들리고 호수가 물결치는 상태"]
    elif spd>=39 and spd<=49:
        return ["Strong breeze", "큰 나뭇가지가 흔들리고 우산을 지탱하기 힘든 상태"]
    elif spd>=50 and spd<=61:
        return ["Near gale", "나무 전체가 흔들리며, 바람을 맞서 걷기가 어려운 상태"]
    elif spd>=62 and spd<=74:
        return ["Gale", "작은 나뭇가지가 꺾이며, 바람을 맞서서는 걸을 수 없는 상태"]
    elif spd>=75 and spd<=88:
        return ["Strong Gale", "굴뚝이 넘어지는 등 가옥에 다소 손해가 발생하는 상태"]
    elif spd>=89 and spd<=102:
        return ["Storm", "수목이 뿌리째 뽑히고 가옥에 큰 손해가 일어나는 상태"]
    elif spd>=103 and spd<=117:
        return ["Violent storm", "광범위한 파괴가 발생하는 상태"]
    elif spd>=118:
        return ["Hurricane", "최고 단계의 바람입니다!! 극히 주의를 바라는 상태"]
#============================================================================================
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
#============================================================================================
driver=set_chrome_driver()
driver.implicitly_wait(5)

driver.get('https://earth.nullschool.net/#current/wind/surface/level/orthographic=-232.22,35.08,5038/loc=128.094,35.180')
driver.maximize_window()

while True:
    NOW=DT.now()
    TIME_INFO=NOW.strftime('%Y-%m-%d %H:%M:%S')
    DATE=TIME_INFO[:11]
    MIN=TIME_INFO[14:16]
    SEC=TIME_INFO[17:19]
    
    INFO_ORIGIN=str(driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[2]/div').text)
    
    num=0
    for w in INFO_ORIGIN:
        if w=="@":
            num=INFO_ORIGIN.index("@")
            break
        
    time.sleep(0.5)
    SPD=int(re.sub(r'[^0-9]', '', INFO_ORIGIN[num+1:]))
    time.sleep(0.5)
    
    INFO=WIND_FORCE(SPD)
    STEP=INFO[0]
    MSG=INFO[1]
    
    if MIN=="00" or MIN=="30" or MIN=="57":
        if SEC=="00":
            smtp=smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(meID, mePW)

            MAIL=MIMEMultipart()
            MAIL['Subject']="Hwi가 보낸 태풍 알림입니다."

            TOTAL_MSG="<<태풍 알림>> - {0}\n*진주 풍속 = {1} km/h\n\n*{2}로 구분된 {3}입니다.\n(구분 기준 : 보퍼트 풍력 계급)\n\n※이 메일은 Hwi의 컴퓨터에서 자동으로 발송되었습니다.".format(TIME_INFO, SPD, STEP, MSG)
            #MAIL=MIMEText(TOTAL_MSG)
            MSG_PART=MIMEText(TOTAL_MSG, "plain")
            MAIL.attach(MSG_PART)
            
            driver.get('https://earth.nullschool.net/#current/wind/surface/level/orthographic=-232.22,35.08,5038/loc=128.094,35.180')
            time.sleep(1)

            driver.save_screenshot("./Typhoon_Screenshot_"+str(DATE)+".png")
            time.sleep(3)
            IMG="./Typhoon_Screenshot_"+str(DATE)+".png"

            with open(IMG, 'rb') as CAP:
                img = MIMEImage(CAP.read())
                img.add_header('Content-Disposition','attachment', filename=IMG)
                MAIL.attach(img)

            for num in range(4, len(info)):
                print(num-3,"명째")
                smtp.sendmail("meID", info[num], MAIL.as_string())


            smtp.quit()
            print("전송 완료")
