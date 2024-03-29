from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.Locator import Locator
from utilities.BaseElementClass import BaseElement


class BasePageClass:
    _URL = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        # add wait for page loading
        self.driver.get(self._URL)

    def get_page_url(self):
        return self.driver.current_url
