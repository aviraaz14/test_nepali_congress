import page
import time
import unittest
import pytest
from selenium import webdriver

class nepaliCongress(unittest.TestCase):
       
    def setUp(self):
        self.driver = webdriver.Chrome('D:/selenium/chromedriver_win32/chromedriver.exe')
        self.driver.get('http://www.nepalicongress.org/')
        self.driver.maximize_window()
        
    def test_title(self):
        print ("TEST1: TITLE TEST")
        landing_page = page.LandingPage(self.driver)
        message = "Title of website is not Nepali Congress:"
        self.assertTrue(landing_page.is_title_matches(), message)
        
    def test_language_changer(self):
        print ("TEST2: LANGUAGE CHANGING TEST")
        message = 'language is not changing'
        landing_page = page.LandingPage(self.driver)
        landing_page.language_change()
        # print (landing_page.is_languages_changing())
        self.assertTrue(landing_page.is_languages_changing(), message)
        # or self.assertEqual(landing_page.is_languages_changing(),'Documents')
    
    def test_on_navbar_link(self):
        print('Test3: Navar link check')
        landing_page = page.LandingPage(self.driver)
        landing_page.is_navbar_link_working()
        self.assertEqual(landing_page.result_of_navbar_link(), 'Circulars')
    
    def test_signup_form(self):
        print('Test4:Signup form check with new user data')
        accounts_page = page.AccountsPage(self.driver)
        accounts_page.navigate_to_signup_form()
        accounts_page.filling_first_part_of_the_registration_form()
        accounts_page.click_next_button()
        self.assertEqual(accounts_page.click_next_button_result(), 'Nearest Landmark')
        time.sleep(5)  
        accounts_page.filling_second_part_of_the_registration_form()
        message = 'not working'
        self.assertTrue(accounts_page.result_of_submiting_signup_form(), message)
    
    def test_registering_new_user_without_data(self):
        print('Test5: SignUp form check without user data')
        accounts_page = page.AccountsPage(self.driver)
        accounts_page.navigate_to_signup_form()
        accounts_page.click_next_button()
        message = 'You cannot signup with blank field'
        expected_result = "Please fill enter the form"
        real_result = accounts_page.click_next_button_result()
        self.assertEqual(expected_result, real_result, message)        
             
          
        
    
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()