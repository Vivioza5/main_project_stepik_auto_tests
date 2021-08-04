from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link1="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product=ProductPage(browser, link1)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.item_added_to_cart()
    product.item_added_to_cart_right()