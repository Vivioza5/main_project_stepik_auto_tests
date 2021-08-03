from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time




class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # self.current_url=browser.current_url


    def open(self):
        self.browser.get(self.url)
        time.sleep(15)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
           return False
        return True


