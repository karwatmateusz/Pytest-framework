from utilities.BaseTestClass import BaseTestClass
import pytest
from utilities.Logger import Logger
import logging
from pages.FormPage import FormPage


class TestForm(BaseTestClass):

    log = Logger(logging.DEBUG)

    @pytest.mark.form
    def test_mandatory_fields(self):
        form_page = FormPage(self.driver)
        form_page.go()
        form_page.fill_mandatory_fields()
        form_page.submit_form()
