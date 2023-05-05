from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.Locator import Locator
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePageClass):
    _URL = "https://automationintesting.online/#/admin"
    username_locator = Locator("input[data-testid='username']")
    password_locator = Locator("input[data-testid='password']")
    login_locator = Locator("button[data-testid='submit']")
    error_border_username = Locator("input[style*='red'][data-testid='username']")
    error_border_password = Locator("input[style*='red'][data-testid='password']")
    room_listing_locator = Locator("div[data-testid='roomlisting']")

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
        return BaseElement(self.driver, self.room_listing_locator).is_visible()

    def is_error_border_visible(self):
        try:
            return BaseElement(self.driver, self.error_border_username).is_visible()
        except TimeoutException as e:
            return False
