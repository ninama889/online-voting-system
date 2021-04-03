from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('chromedriver.exe')

    def tearDown(self): 
        self.browser.close()


    def login_test(self):
        self.browser.get('http://127.0.0.1:8000/register/')
        self.browser.maximize_window() 
    
        #signup testing
        self.browser.find_element_by_name("username").send_keys("dharu5")
        time.sleep(1)
    
        self.browser.find_element_by_name("first_name").send_keys("mittal")
        time.sleep(1)
        self.browser.find_element_by_name("last_name").send_keys("hatvani")
        time.sleep(1)
        self.browser.find_element_by_name("email").send_keys("hatvanimittal@gmail.com")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("123456")
        time.sleep(1)
        self.browser.find_element_by_name("confirm_password").send_keys("123456")
        time.sleep(1)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(5)

        self.browser.get('http://127.0.0.1:8000/login/')
        #login testing
        
        self.browser.find_element_by_name("username").send_keys("dharu5")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("123456")
        time.sleep(1)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(3)

        #clicktovote
        self.browser.find_element_by_class_name("clicktovote").click()
        time.sleep(3)
