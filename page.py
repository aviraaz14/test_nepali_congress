import re
import time
from element import BasePageElement
from locators import languageLocators
from locators import navbarLocators
from locators import accountLocators
from locators import register_pageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        
class LandingPage(BasePage):
    def is_title_matches(self):
        return "Nepali Congress" in self.driver.title
    
    def language_change(self):
        global language_to_English
        language_to_English = self.driver.find_element(*languageLocators.ENGLISH)
        language_to_Nepali = self.driver.find_element(*languageLocators.NEPALI)
        language_to_English.click()
        language_to_Nepali.click()
        self.driver.implicitly_wait(5)
        language_to_English.click()
        time.sleep(3)
        
    def is_languages_changing(self):
        # assert browser.page_source.find("Cyberoam Captive Portal") 
        # a = self.driver.page_source.find('Documents')
        # return a
        src = self.driver.page_source
        text_to_search = re.search("documents", src) #or re.findall
        # return text_to_search[0]
        if text_to_search:
            return True
        else:
            return False
         
    def is_navbar_link_working(self):
        # actions = ActionChains(self.driver)
        
        self.driver.find_element(*languageLocators.ENGLISH).click()
        subdomain_link = self.driver.find_element(*navbarLocators.SUBDOMAIN)
        navigate_to_subdomain = subdomain_link.click()
        time.sleep(5)
        online_library_link = self.driver.find_element(*navbarLocators.ONLINE_LIBRARY)
        navigate_to_online_library = online_library_link.click()
        time.sleep(5)
        document_link = self.driver.find_element(*navbarLocators.DOCUMENTS)
        navigate_to_documents = document_link.click()
        time.sleep(5)
        Circulars = self.driver.find_element(*navbarLocators.CIRCULARS)
        navigate_to_circulars = Circulars.click()
    
        
        
        
        
        
        # actions.move_to_element(about_link).move_to_element(subdomain_link).move_to_element(online_library_link)
        # actions.move_to_element(rules_regulations_link).move_to_element(document_link).move_to_element(Circulars).click().perform()
        # time.sleep(3)
        
    def result_of_navbar_link(self):
        src = self.driver.page_source
        text_to_find = re.findall('Circulars', src)
        return text_to_find[0]
    
class AccountsPage(BasePage):
    def navigate_to_signup_form(self):
        language_to_English = self.driver.find_element(*languageLocators.ENGLISH).click()
        go_to_user_page = self.driver.find_element(*accountLocators.ACCOUNTS).click()
        self.driver.implicitly_wait(4)
        add_new_user_page = self.driver.find_element(*accountLocators.REGISTRATION).click()    
        self.driver.implicitly_wait(4)
    
    def filling_first_part_of_the_registration_form(self):
        # language_to_English = self.driver.find_element(*languageLocators.ENGLISH).click()
        # go_to_user_page = self.driver.find_element(*accountLocators.ACCOUNTS).click()
        # self.driver.implicitly_wait(4)
        # add_new_user_page = self.driver.find_element(*accountLocators.REGISTRATION).click()    
        # self.driver.implicitly_wait(4)
        First_name = self.driver.find_element(*register_pageLocators.FIRST_NAME)
        First_name.send_keys('test')
        Last_name = self.driver.find_element(*register_pageLocators.LAST_NAME)
        Last_name.send_keys('test')
        Phone_Number = self.driver.find_element(*register_pageLocators.PHONE_NUM)
        Phone_Number.send_keys('9799999699')
        
        Date_Of_Birth = self.driver.find_element(*register_pageLocators.DOB)
        Date_Of_Birth.click()
        self.driver.implicitly_wait(5)
        actions_on_DOB =  ActionChains(self.driver)
        month_change = self.driver.find_element(*register_pageLocators.MONTH_CHANGER)
        dob_select = self.driver.find_element(*register_pageLocators.DOB_CALENDER)
        actions_on_DOB.move_to_element(month_change).click().perform()
        self.driver.implicitly_wait(5)
        actions_on_DOB.move_to_element(dob_select).click().perform()
        
        Email = self.driver.find_element(*register_pageLocators.EMAIL)
        Email.send_keys('test1@gmail.com')
        Password = self.driver.find_element(*register_pageLocators.PASSWORD)
        Password.send_keys('123456789')
        show_password = self.driver.find_element(*register_pageLocators.SHOW_PASSWORD).click()
        Confirm_Password = self.driver.find_element(*register_pageLocators.CONFIRM_PASSWORD)
        Confirm_Password.send_keys('123456789')
        Select_Gender = self.driver.find_element(*register_pageLocators.GENDER)
        Select_Gender.click()
        self.driver.implicitly_wait(5)
        change_gender = self.driver.find_element(*register_pageLocators.CHANGE_GENDER).click()
        
    
    def click_next_button(self):
        Next_button = self.driver.find_element(*register_pageLocators.NEXT_BUTTON)
        Next_button.click()
        
    def click_next_button_result(self):
        src = self.driver.page_source
        text_to_find = re.findall('Nearest Landmark', src)
        return text_to_find[0]
    
    def filling_second_part_of_the_registration_form(self):
        municipality = self.driver.find_element(*register_pageLocators.MUNICIPALITY)
        municipality.send_keys('lalitpurs')
        district = self.driver.find_element(*register_pageLocators.DISTRICT)
        district.send_keys('Lalitpur')
        ward_number = self.driver.find_element(*register_pageLocators.WARD_NO)
        ward_number.send_keys('06')
        city = self.driver.find_element(*register_pageLocators.CITY)
        city.send_keys('Lamatar')
        provience = self.driver.find_element(*register_pageLocators.PROVINCE)
        provience.send_keys('Bagmati')
        nearest_landmark = self.driver.find_element(*register_pageLocators.NEAREST_LANDMARK)
        nearest_landmark.send_keys('Khai')
        address = self.driver.find_element(*register_pageLocators.ADDRESS)
        address.send_keys('khai')
        click_next_button = self.driver.find_element(*register_pageLocators.SECOND_PAGE_NEXT_BUTTON).click()
        time.sleep(10)
    
    def result_of_submiting_signup_form(self):
        src = self.driver.page_source
        text_to_find = re.findall('VERIFICATION', src)
        if text_to_find:
            return True
        else:
            return False
        
        
        
    
        
    
        
        