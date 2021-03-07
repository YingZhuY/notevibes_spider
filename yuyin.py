import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import json
import time
import os   #os模块中包含很多操作文件和目录的函数
import sys

"""
cookie_str=r'...'
cookies={}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
"""

#填写webdriver的保存目录
browser = webdriver.Chrome('D:/Anaconda/Anaconda3/chromedriver.exe')

url = 'https://notevibes.com/cabinet.php'
browser=webdriver.Chrome()
browser.get(url)    #response=
#print(response.status_code)

"""尝试cookie登录
#首先清除由于浏览器打开已有的cookies
browser.delete_all_cookies()

with open('cookies.txt','r') as cookief:
    #使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)

    # 方法1 将expiry类型变为int
    for cookie in cookieslist:
        #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        browser.add_cookie(cookie)
#browser.refresh()
browser.get(url)
"""

time.sleep(100)         # 等待网页输入邮箱的时间
print("start new page")
browser.get(url)
WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.NAME,'voice')))     # 等待，判断元素是否出现
select = browser.find_element_by_name('voice')
# 选中普通话下的第一个选项
# <option id="google" value="cmn-CN-Wavenet-A">Mandarin Chinese - Ah Cy  </option>
classSelectValue="cmn-CN-Wavenet-A"
Select(select).select_by_value(classSelectValue)
time.sleep(2)
#Select(browser.find_element_by_tag_name("voice")).select_by_value(classSelectValue)

i=1
#获取待转换文件夹中的文件名称列表   
filepath='D:\\dream\\ToSpeech\\text\\'     #文件路径
filenames = os.listdir(filepath)

for filename in filenames:      #遍历文件夹
    #遍历单个文件
    temppath=filepath+filename
    tempf=open(temppath,'r',encoding='utf-8')
    s=tempf.read()
    if(len(s)>10000):
        s=s[0:10000]
    # 注意：输入文字有长度限制
    # <div contenteditable="true" id="editor" maxlength="20000" placeholder="Enter text here...">
    # 拿到输入框
    input = browser.find_element_by_xpath("//*[@id='editor']")
    # 清空之前的内容
    input.clear()
    # 输入文本
    input.send_keys(s)
    input.send_keys(Keys.RETURN)
    browser.find_element_by_id("btnSubmit").click()
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadpanel"]/div/div[2]/div/a')))
    button.click()
    print("已经下载文件语音 "+str(i))
    if(i>9):
        break
    i+=1
    time.sleep(5)


