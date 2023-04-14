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
        assert "Thank you" in form_page.get_success_message()

    @pytest.mark.form
    def test_empty_mandatory_field(self):
        form_page = FormPage(self.driver)
        form_page.go()
        form_page.fill_non_mandatory_fields()
        form_page.submit_form()
        assert "Your form has encountered a problem" in form_page.get_error_message()

    @pytest.mark.form
    def test_all_fields_filled(self):
        form_page = FormPage(self.driver)
        form_page.go()
        form_page.fill_mandatory_fields()
        form_page.fill_non_mandatory_fields()
        assert "Thank you" in form_page.get_success_message()
