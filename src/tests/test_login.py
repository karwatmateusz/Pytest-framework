import pytest
import allure
from src.ATframework.utilities.BaseTestClass import BaseTestClass
from src.ATframework.pages.LoginPage import LoginPage
from utilities.logger import Logger
import logging


class TestLogin(BaseTestClass):

    log = Logger(logging.DEBUG)

    valid_credentials = ["tomsmith", "SuperSecretPassword!"]
    invalid_credentials = ["test", "test"]

    @pytest.mark.login
    @allure.title("This test has a custom title")
    def test_login_page_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.go()
        login_page.username_input(self.valid_credentials[0])
        login_page.password_input(self.valid_credentials[1])
        login_page.login_button_click()
        assert login_page.is_user_logged(), "User not logged in"

    @pytest.mark.login
    @pytest.mark.xfail(raises=AssertionError, reason="Should fail only on assertion")
    def test_login_page_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.go()
        # login_page.username_input(self.invalid_credentials[0])
        # login_page.password_input(self.invalid_credentials[1])
        # login_page.login_button_click()
        login_page.login_to_system(
            self.invalid_credentials[0], self.invalid_credentials[1]
        )
        assert login_page.is_user_logged(), "User logged in"
