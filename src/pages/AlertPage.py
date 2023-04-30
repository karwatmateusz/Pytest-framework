from utilities.BasePageClass import BasePageClass
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseElementClass import BaseElement
from utilities.Locator import Locator
from selenium.webdriver.common.alert import Alert


class AlertPage(BasePageClass):

    _URL = "https://the-internet.herokuapp.com/javascript_alerts"
    alert_button_locator = Locator('//button[contains(.,"Alert")]', By.XPATH)
    confirm_button_locator = Locator('//button[contains(.,"Confirm")]', By.XPATH)
    prompt_button_locator = Locator('//button[contains(.,"Prompt")]', By.XPATH)
    result_box = Locator("#result")

    def open_alert_box(self):
        alert_button = BaseElement(self.driver, self.alert_button_locator)
        alert_button.click_field()

    def open_confirm_box(self):
        confirm_button = BaseElement(self.driver, self.confirm_button_locator)
        confirm_button.click_field()

    def open_prompt_box(self):
        prompt_button = BaseElement(self.driver, self.prompt_button_locator)
        prompt_button.click_field()

    def alert_input(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)

    def confirm_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def cancel_alert(self):
        Alert(self.driver).dismiss()

    def get_result_box_text(self):
        result_box = BaseElement(self.driver, self.result_box)
        return result_box.text
