from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.Locator import Locator
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePageClass):
    _URL = "https://the-internet.herokuapp.com/login"
    username_locator = Locator("#username")
    password_locator = Locator("#password")
    login_locator = Locator("#login > button")
    error_message_locator = Locator("div > .error")

    def username_input(self, username):
        username_field = BaseElement(self.driver, self.username_locator)
        username_field.insert_text(username)

    def password_input(self, password):
        password_field = BaseElement(self.driver, self.password_locator)
        password_field.insert_text(password)

    def login_button_click(self):
        login_button = BaseElement(self.driver, self.login_locator)
        login_button.click_element()

    def login_to_system(self, username, password):
        self.username_input(username)
        self.password_input(password)
        self.login_button_click()

    def is_user_logged(self):
        return "secure" in self.get_page_url()

    def is_error_message_visible(self):
        try:
            BaseElement(self.driver, self.error_message_locator)
        except TimeoutException as e:
            return False
        else:
            return True
