import pytest
import allure
from utilities.BaseTestClass import BaseTestClass
from pages.LoginPage import LoginPage
from utilities.Logger import Logger
import logging


class TestLogin(BaseTestClass):

    log = Logger(logging.DEBUG)
    valid_credentials = ["tomsmith", "SuperSecretPassword!"]
    invalid_credentials = ["test", "test"]
    login_page = None

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.go()

    @pytest.mark.login
    @allure.title("Test to check login functionality with valid credentials")
    def test_login_page_valid_credentials(self):
        # login_page.username_input(self.valid_credentials[0])
        # login_page.password_input(self.valid_credentials[1])
        # login_page.login_button_click()
        # assert login_page.is_user_logged(), "User not logged in"
        self.login_page.login_to_system(
            self.valid_credentials[0], self.valid_credentials[1]
        )
        if self.login_page.is_user_logged():
            self.log.info("User successfully logged in with valid credentials")
        else:
            self.log.error(
                f"User not logged in with credentials: username - {self.valid_credentials[0]}, password - {self.valid_credentials[1]}"
            )
            pytest.fail("User should log in")

    @pytest.mark.login
    @allure.title("Test to check login functionality with invalid credentials")
    @pytest.mark.xfail(reason="Should fail only on assertion")
    def test_login_page_invalid_credentials(self):
        # login_page.username_input(self.invalid_credentials[0])
        # login_page.password_input(self.invalid_credentials[1])
        # login_page.login_button_click()
        self.login_page.login_to_system(
            self.invalid_credentials[0], self.invalid_credentials[1]
        )
        # assert login_page.is_user_logged(), "User logged in"
        if not self.login_page.is_user_logged():
            self.log.info(f"User correctly not logged in with invalid credentials")
            pytest.fail("User correctly not logged in")
        else:
            self.log.error(
                f"User logged in with credentials: username - {self.invalid_credentials[0]}, password - {self.invalid_credentials[1]}"
            )
