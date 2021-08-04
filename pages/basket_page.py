from pages.base_page import BasePage
from pages.locators import MainPageLocators, BasketPageLocators



class BasketPage(BasePage):

#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a
    def should_be_basket_page(self):
        print(self.browser.current_url)
        assert "basket" in self.browser.current_url , "Login link is not presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM),\
             "Items in basket is presented, but should not be"