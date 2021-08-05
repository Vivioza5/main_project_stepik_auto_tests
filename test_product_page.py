import time
import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.need_review
class TestGuestAndUserAddProductToBasketAndGoToLoginPage:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    def test_user_can_add_product_to_basket(self, browser):
        email = (str(time.time())) + "@fakemail.org"
        password = str((time.time()) +20)
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        product = ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.item_added_to_cart()
        product.item_added_to_cart_right()

    def test_guest_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.item_added_to_cart()
        product.item_added_to_cart_right()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()

    def test_guest_can_go_login_link_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self, browser):
        product = ProductPage(browser, link)
        product.open()
        product.should_not_be_success_message()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product=ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.solve_quiz_and_get_code()
        product.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self,browser):
        product=ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.solve_quiz_and_get_code()
        product.should_not_be_success_message_visible()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()








