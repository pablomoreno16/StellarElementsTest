from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from web_tests.utils.helpers import Helpers
from selenium.common.exceptions import TimeoutException


class ThankYouPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    title = (By.XPATH, "//h2[text()='Thanks for throwing us a bone.']")

    # Page Actions
    def is_displayed(self):
        wait = WebDriverWait(self.driver, int(Helpers.get_config_data("explicit_wait")))
        try:
            wait.until(lambda d: d.find_element(*self.title).is_displayed())
            return True
        except TimeoutException:
            return False
