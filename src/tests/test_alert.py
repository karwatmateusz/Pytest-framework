import pytest
import allure
from utilities.BaseTestClass import BaseTestClass
from pages.LoginPage import LoginPage
from utilities.Logger import Logger
import logging
from pages.AlertPage import AlertPage


class TestAlert(BaseTestClass):

    log = Logger(logging.DEBUG)
    input_text = "Input field text"

    # @pytest.mark.alert
    def test_alert_box(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_alert_box()
        alert_page.confirm_alert()
        result_text = alert_page.get_result_box_text()
        assert "successfully" in result_text, self.log.error(
            f"Alert test failed, text: {result_text}"
        )

    # @pytest.mark.alert
    def test_confirm_box_ok(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_confirm_box()
        alert_page.confirm_alert()
        result_text = alert_page.get_result_box_text()
        assert "Ok" in result_text, self.log.error(
            f"OK confirm alert test failed, text: {result_text}"
        )

    # @pytest.mark.alert
    def test_confirm_box_cancel(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_confirm_box()
        alert_page.cancel_alert()
        result_text = alert_page.get_result_box_text()
        assert "Cancel" in result_text, self.log.error(
            f"Cancel confirm alert test failed, text: {result_text}"
        )

    @pytest.mark.alert
    def test_prompt_box_with_input(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_prompt_box()
        alert_page.alert_input(self.input_text)
        alert_page.confirm_alert()
        result_text = alert_page.get_result_box_text()
        assert self.input_text in result_text, self.log.error(
            f"Prompt alert test with input failed, text: {result_text}"
        )

    @pytest.mark.alert
    def test_prompt_box_empty(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_prompt_box()
        alert_page.confirm_alert()
        result_text = alert_page.get_result_box_text()
        print(f"result text to {result_text}")
        assert "You entered:" == result_text, self.log.error(
            f"Prompt alert test with empty input failed, text: {result_text}"
        )

    @pytest.mark.alert
    def test_prompt_box_cancel(self):
        alert_page = AlertPage(self.driver)
        alert_page.go()
        alert_page.open_prompt_box()
        alert_page.cancel_alert()
        result_text = alert_page.get_result_box_text()
        assert "null" in result_text, self.log.error(
            f"Prompt alert cancel test failed, text: {result_text}"
        )
