from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.Locator import Locator


class LoginPage(BasePageClass):

    _URL = "sample url"
    sample_locator = Locator('sample_css_locator')
    
    def __init__(self, driver):
        self.driver = driver
    
    def field_input(self, text):
        input_field = BaseElement(self.driver, self.sample_locator)
        #do some stuff with field using methods from BaseElement class

    def get_url(self):
        return self.driver.current_url