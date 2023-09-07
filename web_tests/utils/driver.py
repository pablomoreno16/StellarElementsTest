import os
from selenium.webdriver.chrome.service import Service
from web_tests.utils.helpers import Helpers
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class DriverFactory:
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            print("initializing the driver")
            if os.environ.get('browser', Helpers.get_config_data("browser")) == 'chrome':
                if os.environ.get('headless', Helpers.get_config_data("headless")):
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("window-size=1920,1080")
                    cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
                else:
                    cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                    cls.driver.maximize_window()
            else:
                raise NotImplementedError
        cls.driver.implicitly_wait(os.environ.get('implicitly_wait', Helpers.get_config_data("implicitly_wait")))
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
