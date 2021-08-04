from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASCKET_BTN=(By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME=(By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE=(By.CLASS_NAME, "price_color")
    PRODUCT_BASCKET_MESSAGE=(By.ID,"messages")

