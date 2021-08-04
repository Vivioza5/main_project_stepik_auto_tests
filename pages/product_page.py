import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_cart_foo(self):
       product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
       product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
       print(product_name.text)
       print(product_price.text)
       self.product_name=product_name.text
       self.product_price=product_price.text
       add_to_bascket = self.browser.find_element(*ProductPageLocators.ADD_BASCKET_BTN)
       add_to_bascket.click()




    def item_added_to_cart(self):
        time.sleep(20)
        bascket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_BASCKET_MESSAGE)
        bascket_message_name=bascket_message.find_element(By.CSS_SELECTOR, ".alertinner strong")
        bascket_message_price=bascket_message.find_element(By.CSS_SELECTOR, ".alertinner p")
        # print(bascket_message_name.text)
        # print(bascket_message_price.text)
        self.bascket_message_name=bascket_message_name.text
        self.bascket_message_price=bascket_message_price.text

    def item_added_to_cart_right(self):
        product_name=self.product_name
        product_price=self.bascket_message_price
        bascket_message_name=self.bascket_message_name
        bascket_message_price=self.bascket_message_price
        assert product_name==bascket_message_name,  "item_added_to_cart_wrong"
        assert product_price in bascket_message_price,  "item_added_to_cart_wrong"


       # cur_url=self.browser.current_url
       # print(cur_url)

       # return LoginPage(browser=self.browser, url=self.browser.current_url)
#content_inner > article > div.row > div.col-sm-6.product_main


    # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"