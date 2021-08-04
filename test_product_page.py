import pytest

from .pages.locators import MainLocators
from .pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                       pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link1="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product=ProductPage(browser, link)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.item_added_to_cart()
    product.item_added_to_cart_right()
    # product.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product=ProductPage(browser, link)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product=ProductPage(browser, link)
    product.open()
    product.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    product=ProductPage(browser, link)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.should_not_be_success_message_visible()