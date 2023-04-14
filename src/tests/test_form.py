from utilities.BaseTestClass import BaseTestClass
import pytest
from utilities.Logger import Logger
import logging
from pages.FormPage import FormPage


class TestForm(BaseTestClass):

    log = Logger(logging.DEBUG)
    form_page = None

    def setup_method(self):
        self.form_page = FormPage(self.driver)
        self.form_page.go()

    @pytest.mark.form
    def test_mandatory_fields(self):
        self.form_page.fill_mandatory_fields()
        self.form_page.submit_form()
        assert "Thank you" in self.form_page.get_success_message()

    @pytest.mark.form
    def test_empty_mandatory_field(self):
        self.form_page.fill_non_mandatory_fields()
        self.form_page.submit_form()
        assert (
            "Your form has encountered a problem" in self.form_page.get_error_message()
        )

    @pytest.mark.form
    def test_all_fields_filled(self):
        self.form_page.fill_mandatory_fields()
        self.form_page.fill_non_mandatory_fields()
        self.form_page.submit_form()
        assert "Thank you" in self.form_page.get_success_message()
