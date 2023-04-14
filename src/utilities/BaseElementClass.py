from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.Locator import Locator
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BaseElement:
    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator
        self.element = self.is_element_present()

    def insert_text(self, text):
        # self.element.clear()
        self.element.send_keys(text)

    def click_element(self):
        try:
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element)
            self.element.location_once_scrolled_into_view
            self.is_element_clickable().click()
            # self.element.click()
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not clickable") from e

    def clear_field(self):
        self.element.clear()

    def get_text(self):
        return self.element.text

    def is_selected(self):
        return self.element.is_selected()

    def is_visible(self):
        try:
            self.is_element_visible()
            return True
        except TimeoutException:
            return False

    def is_element_present(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located(
                    (self.locator.method, self.locator.location)
                )
            )
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not found") from e
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element {self.locator} not found") from e

    def is_element_visible(self):
        try:
            self.is_element_present()
            return self.element.is_displayed()
        except TimeoutException:
            return False

    def is_element_clickable(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.element_to_be_clickable(self.element)
            )
        except TimeoutException as e:
            raise TimeoutException(f"Element {self.locator} not clickable") from e
