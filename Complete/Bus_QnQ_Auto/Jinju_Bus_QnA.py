from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

f = open('./Login_info2.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

ID=info[1]
PW=info[3]

HEAD = info[5]

for i in range(1,6):
    globals()['BODY_{}'.format(i)]=info[i+6]
    
#=====================================================================================================
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver=set_chrome_driver()
driver.implicitly_wait(5)

driver.get('http://jinjuterminal.kr/index.php?mid=home&act=dispMemberLoginForm&mode=default')
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="uid"]').send_keys(ID)
driver.find_element(By.XPATH,'//*[@id="upw"]').send_keys(PW)
driver.find_element(By.XPATH,'//*[@id="fo_member_login"]/button').click()

# 고객광장 클릭
driver.find_element(By.XPATH,'//*[@id="wrap"]/header/div/div/div[2]/ul/li[4]/a').click()

# 글쓰기 클릭
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/div[3]/div[1]/a[1]').click()

# 글 제목
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/form/div[1]/input').send_keys(HEAD)
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/form/div[1]/input').send_keys(
    Keys.TAB,
    BODY_1, Keys.ENTER, Keys.ENTER,
    Keys.SPACE, Keys.SPACE, BODY_2, Keys.ENTER, Keys.ENTER,
    Keys.SPACE, Keys.SPACE, BODY_3, Keys.ENTER, Keys.ENTER,
    Keys.SPACE, Keys.SPACE, BODY_4, Keys.ENTER, Keys.ENTER,
    Keys.SPACE, Keys.SPACE, BODY_5)
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/form/div[3]/div[3]/button[3]').click()
time.sleep(1)
driver.quit()
