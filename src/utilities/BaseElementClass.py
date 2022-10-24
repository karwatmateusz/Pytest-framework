from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement():

    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.verify_element(self.locator)

    def insert_text(self, text):
        self.element.send_keys(text)
        return self

    def click_field(self):
        self.element.click()
        return self
        
    def verify_element(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((locator.method, locator.location)))
