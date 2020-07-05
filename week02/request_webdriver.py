'''
pip install selenium
下载chrome driver.exe和浏览器版本保存一致，放到安装目录script目录下
下载地址：http://chromedriver.storage.googleapis.com/index.html
'''
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)

    browser.find_element_by_xpath(
        '//button[contains(@class,"login-button")]').click()
    time.sleep(2)

    browser.find_element_by_xpath(
        '//input[@name="mobileOrEmail"]').send_keys('gkj82@163.com')
    time.sleep(1)  

    browser.find_element_by_xpath(
        '//input[@name="password"]').send_keys('gkjQQ123')
    
    browser.find_element_by_xpath('//button[contains(@class,"sm-button")]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)


except Exception as e:
    print(e)
finally:
    browser.close()
   
