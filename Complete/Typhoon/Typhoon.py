from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#============================================================================================
from datetime import datetime as DT
import smtplib
from email.mime.text import MIMEText
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
def WIND_FORCE(mph):
    if mph>=4 and mph<=7:
        return ["Light breeze", "나뭇잎이 흔들리고 풍향계가 움직이기 시작하는 상태"]
    elif mph>=8 and mph<=12:
        return ["Fresh breeze", "나뭇잎과 가는 가지가 계속 흔들리고 깃발이 가볍게 날리는 상태"]
    elif mph>=13 and mph<=18:
        return ["Moderate breeze", "먼지가 일고 작은 가지가 흔들리는 상태"]
    elif mph>=19 and mph<=24:
        return ["Fresh breeze", "잎이 무성한 나무가 흔들리고 호수가 물결치는 상태"]
    elif mph>=25 and mph<=31:
        return ["Strong breeze", "큰 나뭇가지가 흔들리고 우산을 지탱하기 힘든 상태"]
    elif mph>=32 and mph<=38:
        return ["Near gale", "나무 전체가 흔들리며, 바람을 맞서 걷기가 어려운 상태"]
    elif mph>=39 and mph<=46:
        return ["Gale", "작은 나뭇가지가 꺾이며, 바람을 맞서서는 걸을 수 없는 상태"]
    elif mph>=47 and mph<=54:
        return ["Strong Gale", "굴뚝이 넘어지는 등 가옥에 다소 손해가 발생하는 상태"]
    elif mph>=55 and mph<=63:
        return ["Storm", "수목이 뿌리째 뽑히고 가옥에 큰 손해가 일어나는 상태"]
    elif mph>=64 and mph<=72:
        return ["Violent storm", "광범위한 파괴가 발생하는 상태"]
    elif mph>=73:
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
    MINUTE=TIME_INFO[14:16]
    SEC=TIME_INFO[17:19]

    #print(MINUTE, SEC)
    #print()
    
    MPH=int(str(driver.find_element(By.XPATH,'//*[@id="spotlight-panel"]/div[2]/div').text)[-3:])
    
    INFO=WIND_FORCE(MPH)
    STEP=INFO[0]
    MSG=INFO[1]
    
    if MINUTE=="00" or MINUTE=="30":
        if SEC=="00":
            driver.get('https://earth.nullschool.net/#current/wind/surface/level/orthographic=-232.22,35.08,5038/loc=128.094,35.180')
            time.sleep(1) 
            
            smt=smtplib.SMTP('smtp.gmail.com', 587)
            smt.starttls()
            smt.login(meID, mePW)
            
            TOTAL_MSG="<<태풍 알림>> - {0}\n*현재풍속 = {1} mph\n\n*{2}로 구분된 {3}입니다.\n(구분 기준 : 보퍼트 풍력 계급)\n\n※이 메일은 Hwi의 컴퓨터에서 자동으로 발송되었습니다.".format(TIME_INFO, MPH, STEP, MSG)
            MAIL=MIMEText(TOTAL_MSG)
            MAIL['Subject']="Hwi가 보낸 태풍 알림입니다."

            for num in range(4, len(info)):
                print(num)
                smt.sendmail("meID", info[num], MAIL.as_string())
                smt.quit()
            
    time.sleep(1)
    
#driver.quit()

