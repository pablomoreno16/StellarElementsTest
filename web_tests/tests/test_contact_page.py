import random
import names
import pytest
from web_tests.pages.contact_page import ContactPage
from web_tests.utils.driver import DriverFactory
from web_tests.utils.helpers import Helpers


@pytest.fixture(scope="module")
def browser():
    browser = DriverFactory.get_driver()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def contact_page(browser):
    browser.get(Helpers.get_formatted_url())
    contact_page = ContactPage(browser)
    yield contact_page


def test_contact_form_submission(contact_page):
    print('Fill the form with valid data')
    first_name = names.get_first_name()
    contact_page.enter_first_name(first_name)
    last_name = names.get_last_name()
    contact_page.enter_last_name(last_name)
    email = f"{first_name}.{last_name}@example.com"
    contact_page.enter_work_email(email)
    company_name = f"{names.get_first_name()} inc."
    contact_page.enter_company_name(company_name)
    phone = random.randrange(3000000000, 3010000000)
    contact_page.enter_phone_number(phone)
    contact_page.enter_message(f"This is a test message generated randomly by attaching the phone number: {phone}")
    print('click on submit button')
    thankyou_page = contact_page.click_submit_button(success=True)
    assert thankyou_page.is_displayed()


def test_required_fields(contact_page):
    print('Click on submit button with all fields empty')
    contact_page.click_submit_button()
    print("Verify mandatory first name")
    assert contact_page.is_first_name_error_message_displayed()
    assert contact_page.get_first_name_error_message() == 'This field is required'
    print("Verify mandatory last name")
    assert contact_page.is_last_name_error_message_displayed()
    assert contact_page.get_last_name_error_message() == 'This field is required'
    print("Verify mandatory work email")
    assert contact_page.is_work_email_error_message_displayed()
    assert contact_page.get_work_email_error_message() == 'This field is required'
    print("Verify mandatory company name")
    assert contact_page.is_company_name_error_message_displayed()
    assert contact_page.get_company_name_error_message() == 'This field is required'


@pytest.mark.parametrize("email", ['wrong', 'wrong.email', 'wrong.com', 'wrong@email', '@email.com', '1@email.com'])
def test_valid_email_format(contact_page, email):
    print(f"Enter an invalid email format: {email}")
    contact_page.enter_work_email(email)
    contact_page.click_submit_button()
    print('Verify error message')
    assert contact_page.is_work_email_error_message_displayed()
    assert contact_page.get_work_email_error_message() == 'Incorrect format'


def test_optional_fields(contact_page):
    print('Test the form submission with only required fields filled in.')
    first_name = names.get_first_name()
    contact_page.enter_first_name(first_name)
    last_name = names.get_last_name()
    contact_page.enter_last_name(last_name)
    email = f"{first_name}.{last_name}@example.com"
    contact_page.enter_work_email(email)
    company_name = f"{names.get_first_name()} inc."
    contact_page.enter_company_name(company_name)
    contact_page.click_submit_button()
    thankyou_page = contact_page.click_submit_button(success=True)
    assert thankyou_page.is_displayed()
