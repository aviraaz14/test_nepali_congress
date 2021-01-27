from selenium.webdriver.common.by import By

class languageLocators(object):
    ENGLISH = (By.CSS_SELECTOR, 'li.changeLang:nth-child(1)') 
    NEPALI = (By.CSS_SELECTOR, 'li.changeLang:nth-child(2)')

class navbarLocators(object):
    ABOUT_US = (By.XPATH, '/html/body/div/div/div/main/div/div/div/section[1]/div/div[2]/div/ul/li[1]/div')
    SUBDOMAIN = (By.LINK_TEXT, 'Subdomain')
    ONLINE_LIBRARY = (By.XPATH, '/html/body/div/div/div/main/div/div/div/section[1]/div/div[2]/div/ul/li[3]')
    RULES_AND_REGULATION = (By.LINK_TEXT, 'Rules and Regulations')
    DOCUMENTS = (By.LINK_TEXT, 'Documents')
    CIRCULARS = (By.LINK_TEXT, 'Circulars')
    
class accountLocators(object):
    ACCOUNTS = (By.LINK_TEXT, 'My Congress')
    REGISTRATION = (By.LINK_TEXT, 'REGISTER')

class register_pageLocators(object):
    FIRST_NAME = (By.XPATH, '//input[@id="input-242"]')
    LAST_NAME = (By.XPATH, '//*[@id="input-245"]')
    EMAIL = (By.XPATH, '//*[@id="input-248"]')
    PHONE_NUM = (By.XPATH, '//*[@id="input-251"]')
    DOB = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/input[1]')
    MONTH_CHANGER = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/i[1]')
    DOB_CALENDER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[3]/button[1]/div[1]")
    PASSWORD = (By.XPATH, '//*[@id="input-268"]')
    SHOW_PASSWORD = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    CONFIRM_PASSWORD = (By.XPATH,'//*[@id="input-272"]')
    GENDER = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]')
    CHANGE_GENDER = (By.XPATH, "//div[@class='v-list-item__title'][contains(text(),'Female')]")
    NEXT_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/footer[1]/button[1]")
    SECOND_PAGE_NEXT_BUTTON =(By.XPATH, '/html/body/div/div/div/main/div/div/div/section[2]/div/div/div/div/div/form/div/div[2]/div/footer/button')
                              
    MUNICIPALITY = (By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
    DISTRICT =(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]')
    WARD_NO = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]')
    CITY = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/input[1]')
    PROVINCE = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/input[1]')
    NEAREST_LANDMARK = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/input[1]')
    ADDRESS = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/input[1]')
          