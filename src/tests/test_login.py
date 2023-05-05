import pytest
import allure
from utilities.BaseTestClass import BaseTestClass
from pages.LoginPage import LoginPage
from utilities.Logger import Logger
import logging
from selenium.common.exceptions import TimeoutException


class TestLogin(BaseTestClass):
    log = Logger(logging.DEBUG)
    valid_credentials = ["admin", "password"]
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
        assert self.login_page.is_user_logged(), self.log.error(
            f"User not logged in with credentials: username - {self.valid_credentials[0]}, password - {self.valid_credentials[1]}"
        )

    @pytest.mark.login
    @pytest.mark.xfail(
        raises=TimeoutException,
        reason="User should not be able to log in with invalid credentials",
    )
    @allure.title("Test to check login functionality with invalid credentials")
    def test_login_page_invalid_credentials(self):
        self.login_page.login_to_system(
            self.invalid_credentials[0], self.invalid_credentials[1]
        )
        assert self.login_page.is_user_logged(), self.log.error(
            f"User not logged in with credentials: username - {self.invalid_credentials[0]}, password - {self.invalid_credentials[1]}"
        )

    @pytest.mark.login
    @allure.title("Test to check if error border is visible for invalid credentials")
    def test_login_page_error_visible(self):
        self.login_page.login_to_system(
            self.invalid_credentials[0], self.invalid_credentials[1]
        )
        assert self.login_page.is_error_border_visible(), self.log.error(
            f"Border not visible, user logged in with credentials: username - {self.invalid_credentials[0]}, password - {self.invalid_credentials[1]}"
        )
