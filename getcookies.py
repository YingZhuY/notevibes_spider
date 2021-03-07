from selenium import webdriver
import time
import json

#填写webdriver的保存目录
driver = webdriver.Chrome('D:/Anaconda/Anaconda3/chromedriver.exe')

#记得写完整的url 包括http和https
driver.get('https://notevibes.com/cabinet.php')

#程序打开网页后20秒内手动登陆账户
time.sleep(200)

with open('cookies.txt','w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.close()