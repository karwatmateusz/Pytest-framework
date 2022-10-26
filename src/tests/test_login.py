import pytest
import allure
from utilities.BaseTestClass import BaseTestClass
from utilities.Logger import Logger
import logging


class TestLogin(BaseTestClass):

    log = Logger(logging.DEBUG)

    @pytest.mark.smoke
    @allure.title("This test has a custom title")
    def test_one(self):
        print("lets start test")
        x = 2
        y = 1
        print(f"we add {x} to {y}")
        self.log.debug(f"values: {x} {y}")
        assert x + y == 2, "failed to add"
