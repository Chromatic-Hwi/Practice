from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

f = open('./Login_info.txt', 'r')
lines = f.readlines()
info=[]
for line in lines:
    line = line.strip()
    info.append(line)
f.close()

ID=info[1]
PW=info[3]

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(1)

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
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/form/div[1]/input').send_keys("제목")
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/form/div[1]/input').send_keys(Keys.TAB)

# 글 본문
