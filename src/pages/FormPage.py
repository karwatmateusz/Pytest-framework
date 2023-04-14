from utilities.BasePageClass import BasePageClass, Locator, BaseElement


class FormPage(BasePageClass):
    _URL = "https://www.thegoldbugs.com/"

    # LOCATORS
    FIRST_NAME_LOCATOR = Locator("input[name='fname']")
    LAST_NAME_LOCATOR = Locator("input[name='lname']")
    EMAIL_LOCATOR = Locator("input[name='email']")
    SUBJECT_LOCATOR = Locator(".field-element.text")
    MESSAGE_LOCATOR = Locator("#textarea-yui_3_17_2_1_1664570076619_2730-field")
    CHECKBOX_OPTIONS_LOCATOR = Locator(
        "#checkbox-b5b9cc19-24e5-4c8c-960a-055837723942 div"
    )
    RADIO_BUTTON_OPTIONS_LOCATOR = Locator(
        "input[name='radio-56c0f90d-260f-4304-b624-4635972a6fa9-field']"
    )
    DROPDOWN_SELECTION_LOCATOR = Locator(
        "#select-e1f50715-c8a7-48eb-bc99-2c245676068c-field"
    )
    SURVER_BUTTONS_LOCATOR = Locator(
        "fieldset[id='likert-bc3e2dd1-21ab-487a-ae4e-ab6df785d300']"
    )
    SUBMIT_BUTTON_LOCATOR = Locator("input[type='submit']")
    SUCCESSFULL_SUBMISSION_LOCATOR = Locator(".form-submission-text")
    ERROR_SUBMISSION_LOCATOR = Locator(".field-error")

    # TEST DATA
    user_first_name = "first name"
    user_last_name = "last name"
    user_email = "email@test.com"
    user_subject = "some subject text"
    user_message = "some message text which shoould be longer"
    checkbox_to_select = "No Response Required"
    radio_button_to_select = "Public Show"

    def fill_mandatory_fields(self):
        # first_name = BaseElement(self.driver, self.FIRST_NAME_LOCATOR)
        # first_name.insert_text(self.user_first_name)
        # last_name = BaseElement(self.driver, self.LAST_NAME_LOCATOR)
        # last_name.insert_text(self.user_last_name)
        # email = BaseElement(self.driver, self.EMAIL_LOCATOR)
        # email.insert_text(self.user_email)
        # subject = BaseElement(self.driver, self.SUBJECT_LOCATOR)
        # subject.insert_text(self.user_subject)

        field_locators = {
            "first_name": self.FIRST_NAME_LOCATOR,
            "last_name": self.LAST_NAME_LOCATOR,
            "email": self.EMAIL_LOCATOR,
            "subject": self.SUBJECT_LOCATOR,
        }

        field_values = {
            "first_name": self.user_first_name,
            "last_name": self.user_last_name,
            "email": self.user_email,
            "subject": self.user_subject,
        }
        for field_name, locator in field_locators.items():
            field = BaseElement(self.driver, locator)
            field.insert_text(field_values[field_name])

    def fill_non_mandatory_fields(self):
        message = BaseElement(self.driver, self.MESSAGE_LOCATOR)
        message.insert_text(self.user_message)
        checkbox_options = BaseElement(
            self.driver, self.CHECKBOX_OPTIONS_LOCATOR
        ).get_all_elements()
        for elem in checkbox_options:
            if elem.text == self.checkbox_to_select:
                elem.click()
                break
        radio_button_options = BaseElement(
            self.driver, self.RADIO_BUTTON_OPTIONS_LOCATOR
        ).get_all_elements()
        for elem in radio_button_options:
            if elem.text == self.radio_button_to_select:
                elem.click()
                break

    def submit_form(self):
        submit_button = BaseElement(self.driver, self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click_element()

    def get_success_message(self):
        success_message = BaseElement(self.driver, self.SUCCESSFULL_SUBMISSION_LOCATOR)
        return success_message.get_text()

    def get_error_message(self):
        error_message = BaseElement(self.driver, self.ERROR_SUBMISSION_LOCATOR)
        return error_message.get_text()
