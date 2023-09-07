from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from web_tests.pages.thank_you_page import ThankYouPage


class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    # fields
    first_name_input = (By.ID, "firstname")
    last_name_input = (By.ID, "lastname")
    work_email_input = (By.ID, "email")
    company_name_input = (By.ID, "company")
    phone_number_input = (By.ID, "phone")
    message_textarea = (By.ID, "message")
    submit_button = (By.XPATH, "//button[@type='submit']")
    # errors
    first_name_error_message = (By.XPATH, "//input[@id='firstname']/following-sibling::span[@role='alert']")
    last_name_error_message = (By.XPATH, "//input[@id='lastname']/following-sibling::span[@role='alert']")
    work_email_error_message = (By.XPATH, "//input[@id='email']/following-sibling::span[@role='alert']")
    company_name_error_message = (By.XPATH, "//input[@id='company']/following-sibling::span[@role='alert']")

    # Page Actions
    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_work_email(self, email):
        self.driver.find_element(*self.work_email_input).send_keys(email)

    def enter_company_name(self, company_name):
        self.driver.find_element(*self.company_name_input).send_keys(company_name)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)

    def enter_message(self, message):
        self.driver.find_element(*self.message_textarea).send_keys(message)

    def click_submit_button(self, success=False):
        try:
            # click the object
            self.driver.find_element(*self.submit_button).click()
        except ElementClickInterceptedException:
            # close the cookies pop up
            self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
            # click the object again
            self.driver.find_element(*self.submit_button).click()
        if success:
            return ThankYouPage(self.driver)

    def is_first_name_error_message_displayed(self):
        return self.driver.find_element(*self.first_name_error_message).is_displayed()

    def is_last_name_error_message_displayed(self):
        return self.driver.find_element(*self.last_name_error_message).is_displayed()

    def is_work_email_error_message_displayed(self):
        return self.driver.find_element(*self.work_email_error_message).is_displayed()

    def is_company_name_error_message_displayed(self):
        return self.driver.find_element(*self.company_name_error_message).is_displayed()

    def get_first_name_error_message(self):
        return self.driver.find_element(*self.first_name_error_message).text

    def get_last_name_error_message(self):
        return self.driver.find_element(*self.last_name_error_message).text

    def get_work_email_error_message(self):
        return self.driver.find_element(*self.work_email_error_message).text

    def get_company_name_error_message(self):
        return self.driver.find_element(*self.company_name_error_message).text
