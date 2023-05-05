from utilities.BasePageClass import BasePageClass
from utilities.BaseElementClass import BaseElement
from utilities.Locator import Locator
from selenium.webdriver.common.by import By


class BookingPage(BasePageClass):
    _URL = "https://automationintesting.online/"

    home_banner_image_locator = Locator("img.hotel-logoUrl")

    """ROOM BOOKING LOCATORS"""
    book_button_locator = Locator(
        method=By.XPATH, location="//button[contains(text(),'Book')]"
    )
    cancel_button_locator = Locator(
        method=By.XPATH, location="//button[contains(text(),'Cancel')]"
    )
    input_first_name_locator = Locator("input[aria-label='Firstname']")
    input_last_name_locator = Locator("input[aria-label='Lastname']")
    input_booking_email_locator = Locator("input[aria-label='Email']")
    input_booking_phone_locator = Locator("input[aria-label='Phone']")
    booking_successful_popup = Locator(".ReactModal__Content")

    """CONTACT FORM LOCATORS"""
    input_name_locator = Locator("input[data-testid='ContactName']")
    input_contact_email_locator = Locator("input[data-testid='ContactEmail']")
    input_contact_phone_locator = Locator("input[data-testid='ContactPhone']")
    input_message_subject_locator = Locator("input[data-testid='ContactSubject']")
    input_message_description_locator = Locator(
        "textarea[data-testid='ContactDescription']"
    )
    submit_contact_button_locator = Locator("#submitContact")
    contact_form_successful_message = Locator(
        method=By.XPATH, location="//h2[contains(text(),'Thanks')]"
    )

    """CONTACT FORM"""

    def fill_contact_form(
        self, name, email, phone_number, message_subject, message_description
    ) -> None:
        self.enter_name(name)
        self.enter_email(email)
        self.enter_phone_number(phone_number)
        self.enter_message_subject(message_subject)
        self.enter_message_description(message_description)
        self.submit_contact_form()

    def enter_name(self, name):
        name_field = BaseElement(self.driver, self.input_name_locator)
        name_field.clear_field()
        name_field.insert_text(name)

    def enter_email(self, email):
        email_field = BaseElement(self.driver, self.input_contact_email_locator)
        email_field.clear_field()
        email_field.insert_text(email)

    def enter_phone_number(self, phone_number):
        phone_number_field = BaseElement(self.driver, self.input_contact_phone_locator)
        phone_number_field.clear_field()
        phone_number_field.insert_text(phone_number)

    def enter_message_subject(self, message_subject):
        message_subject_field = BaseElement(
            self.driver, self.input_message_subject_locator
        )
        message_subject_field.clear_field()
        message_subject_field.insert_text(message_subject)

    def enter_message_description(self, message_description):
        message_description_field = BaseElement(
            self.driver, self.input_message_description_locator
        )
        message_description_field.clear_field()
        message_description_field.insert_text(message_description)

    def submit_contact_form(self):
        submit_form = BaseElement(self.driver, self.submit_contact_button_locator)
        submit_form.click_element()

    """BOOKING"""

    def open_room_information(self):
        book_button = BaseElement(self.driver, self.book_button_locator)
        book_button.click_element()

    def enter_first_name(self, first_name):
        first_name_field = BaseElement(self.driver, self.input_first_name_locator)
        first_name_field.clear_field()
        first_name_field.insert_text(first_name)

    def enter_last_name(self, last_name):
        last_name_field = BaseElement(self.driver, self.input_last_name_locator)
        last_name_field.clear_field()
        last_name_field.insert_text(last_name)

    def enter_email(self, email):
        email_field = BaseElement(self.driver, self.input_booking_email_locator)
        email_field.clear_field()
        email_field.insert_text(email)

    def enter_phone_number(self, phone_number):
        phone_number_field = BaseElement(self.driver, self.input_booking_phone_locator)
        phone_number_field.clear_field()
        phone_number_field.insert_text(phone_number)

    def select_booking_days(self, number_of_days):
        pass

    def submit_booking_form(self):
        book_button = BaseElement(self.driver, self.book_button_locator)
        book_button.click_element()

    def fill_booking_form(self, first_name, last_name, email, phone):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_phone_number(phone)

    def is_page_loaded(self):
        # try:
        #     home_banner = BaseElement(
        #         self.driver, self.home_banner_image_locator
        #     ).is_element_present()
        # except TimeoutException:
        #     return False
        # else:
        #     return True
        return BaseElement(self.driver, self.home_banner_image_locator).is_visible()

    def is_form_submitted_successfully(self):
        return BaseElement(
            self.driver, self.contact_form_successful_message
        ).is_visible()

    def is_booking_created_successfully(self):
        return BaseElement(self.driver, self.booking_successful_popup).is_visible()
