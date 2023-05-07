from utilities.BaseTestClass import BaseTestClass
from utilities.Logger import Logger
from pages.BookingPage import BookingPage
import pytest
import logging


class TestBooking(BaseTestClass):
    bookingPage = None
    log = Logger(logging.DEBUG)

    """booking form test data"""
    first_name = "some first name"
    last_name = "some last name"

    """contact form test data"""
    name = "John"
    email = "test@email.com"
    phone_number = "12345678910"
    message_subject = "message subject"
    message_description = "contact form message description"

    def setup_method(self):
        self.bookingPage = BookingPage(self.driver)
        self.bookingPage.go()

    @pytest.mark.booking
    @pytest.mark.smoke
    def test_is_page_loaded(self):
        assert self.bookingPage.is_page_loaded()

    @pytest.mark.booking
    @pytest.mark.regression
    def test_user_can_request_contact(self):
        self.bookingPage.fill_contact_form(
            name=self.name,
            email=self.email,
            phone_number=self.phone_number,
            message_subject=self.message_subject,
            message_description=self.message_description,
        )
        self.bookingPage.submit_contact_form()
        assert self.bookingPage.is_form_submitted_successfully()

    @pytest.mark.booking2
    @pytest.mark.regression
    def test_user_can_book_room(self):
        self.bookingPage.open_room_information()
        self.bookingPage.fill_booking_form(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone_number,
        )
        self.bookingPage.select_booking_days()
        self.bookingPage.submit_booking_form()
        assert self.bookingPage.is_booking_created_successfully()
