from selenium import webdriver
import time
import re

driver = webdriver.Chrome('D:/selenium/chromedriver_win32/chromedriver.exe')
driver.get('https://www.python.org/')
driver.maximize_window()

src = driver.page_source
print(src)
text_to_find = re.findall('Get Started', src)

print (text_to_find)

if text_to_find:
    print ("match")
else:
    print('none')   
     




# register = driver.find_element_by_link_text('REGISTER').click()
# firstname = driver.find_element_by_xpath('//*[@id="input-241"]').send_keys('qwer')







