from utilities.BasePageClass import BasePageClass
from utilities.Locator import Locator
from utilities.BaseElementClass import BaseElement


class FormPage(BasePageClass):
    _URL = "https://www.thegoldbugs.com/"

    # LOCATORS
    first_name_locator = Locator("input[name='fname']")
    last_name_locator = Locator("input[name='lname']")
    email_locator = Locator("input[name='email']")
    subject_locator = Locator(".field-element.text")
    message_locator = Locator("#textarea-yui_3_17_2_1_1664570076619_2730-field")
    checkbox_options_locator = Locator(
        "#checkbox-b5b9cc19-24e5-4c8c-960a-055837723942 div"
    )
    radio_button_options_locator = Locator(
        "radio-56c0f90d-260f-4304-b624-4635972a6fa9 div"
    )
    dropdown_selection_locator = Locator(
        "select-e1f50715-c8a7-48eb-bc99-2c245676068c-field"
    )
    survey_buttons_locator = Locator("#yui_3_17_2_1_1681406804522_478")
    submit_button_locator = Locator("input[type='submit']")

    # TEST DATA
    user_first_name = "first name"
    user_last_name = "last name"
    user_email = "email@test.com"
    user_subject = "some subject text"
    user_message = "some message text which shoould be longer"

    def fill_mandatory_fields(self):
        first_name = BaseElement(self.driver, self.first_name_locator)
        first_name.insert_text(self.user_first_name)
        last_name = BaseElement(self.driver, self.last_name_locator)
        last_name.insert_text(self.user_last_name)
        email = BaseElement(self.driver, self.email_locator)
        email.insert_text(self.user_email)
        subject = BaseElement(self.driver, self.subject_locator)
        subject.insert_text(self.user_subject)

    def fill_non_mandatory_fields(self):
        pass

    def submit_form(self):
        submit_button = BaseElement(self.driver, self.submit_button_locator)
        submit_button.click_element()
