from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)>div>strong")
    CART_COST = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main>.price_color")