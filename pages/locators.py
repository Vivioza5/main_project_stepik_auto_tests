from selenium.webdriver.common.by import By

class MainLocators():
    LINK= "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_PAGE=(By.CSS_SELECTOR, "#basket")
    BASKET_ITEM=(By.CLASS_NAME, "basket-items")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BTN = (By.CSS_SELECTOR,"div.basket-mini.pull-right.hidden-xs a" )
# //*[@id="default"]/header/div[1]/div/div[2]/span/a

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASCKET_BTN=(By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME=(By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE=(By.CLASS_NAME, "price_color")
    PRODUCT_BASCKET_MESSAGE=(By.XPATH,"//*[@id='messages']")
    PRODUCT_BASCKET_MESSAGE_NAME=(By.XPATH,"//*[@id='messages']/div[1]/div")


