import pytest
import allure
from src.ATframework.utilities.BaseTestClass import BaseTestClass


class TestLogin(BaseTestClass):

    @pytest.mark.smoke
    @allure.title("This test has a custom title")
    def test_one(self):
        print("lets start test")
        x = 2
        y = 1
        print(f'we add {x} to {y}')
        assert x+y==2, 'failed to add'
