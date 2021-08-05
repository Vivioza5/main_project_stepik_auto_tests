import time

from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators



class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_page()
        self.should_basket_empty_message()
        self.should_not_be_items_in_basket()


    def should_be_basket_page(self):
        assert "basket" in self.browser.current_url , "Login link is not presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM),\
             "Items in basket is presented, but should not be"

    def should_basket_empty_message(self):
        bascket_empty_message=self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESS)
        assert "Your basket is empty." in bascket_empty_message.text,\
             "Items in basket is presented, but should not be"