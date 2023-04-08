import pytest
import allure
from utilities.BaseTestClass import BaseTestClass
from pages.LoginPage import LoginPage
from utilities.Logger import Logger
import logging
from pages.AlertPage import AlertPage
import selenium.common.exceptions.UnexpectedAlertPresentException()


class TestLogin(BaseTestClass):

    log = Logger(logging.DEBUG)

    @pytest.mark.alert
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
    def test_confirm_box(self):
        pass

    # @pytest.mark.alert
    def test_prompt_box(self):
        pass
