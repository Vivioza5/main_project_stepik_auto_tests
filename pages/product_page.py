import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_cart_foo(self):
       product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
       product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
       self.product_name = product_name.text
       self.product_price = product_price.text
       add_to_bascket = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BTN)
       add_to_bascket.click()

    def item_added_to_cart(self):
        # time.sleep(20)
        basket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_MESSAGE)
        basket_message_name=self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_MESSAGE_NAME)
        basket_message_price=basket_message.find_element(By.CSS_SELECTOR, ".alertinner p")
        print(basket_message_name.text)
        # print(basket_message_price.text)
        self.basket_message_name=basket_message_name.text
        self.basket_message_price=basket_message_price.text

    def item_added_to_cart_right(self):
        # time.sleep(200)
        product_name=self.product_name
        product_price=self.basket_message_price
        basket_message_name=self.basket_message_name
        basket_message_price=self.basket_message_price
        assert product_name in basket_message_name,  "item_added_to_cart_wrong"
        assert product_price in basket_message_price,  "item_added_to_cart_wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_BASKET_MESSAGE_NAME),\
            "Success message is presented, but should not be"

    def should_not_be_success_message_visible(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_BASKET_MESSAGE_NAME),\
            "Success message is presented, but should not be"


