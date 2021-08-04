import time

from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
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
        # time.sleep(20)
        bascket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_BASCKET_MESSAGE)
        bascket_message_name=self.browser.find_element(*ProductPageLocators.PRODUCT_BASCKET_MESSAGE_NAME)
        bascket_message_price=bascket_message.find_element(By.CSS_SELECTOR, ".alertinner p")
        print(bascket_message_name.text)
        # print(bascket_message_price.text)
        self.bascket_message_name=bascket_message_name.text
        self.bascket_message_price=bascket_message_price.text

    def item_added_to_cart_right(self):
        time.sleep(200)
        product_name=self.product_name
        product_price=self.bascket_message_price
        bascket_message_name=self.bascket_message_name
        bascket_message_price=self.bascket_message_price
        assert product_name in bascket_message_name,  "item_added_to_cart_wrong"
        assert product_price in bascket_message_price,  "item_added_to_cart_wrong"

# is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def should_not_be_success_message(self):

        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_BASCKET_MESSAGE_NAME),\
            "Success message is presented, but should not be"

    # is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
    def should_not_be_success_message_visible(self):

        assert self.is_disappeared(*ProductPageLocators.PRODUCT_BASCKET_MESSAGE_NAME),\
            "Success message is presented, but should not be"


