from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)>div>strong")
    CART_COST = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main>.price_color")

class CartPageLocators:
    PRODUCTS_MODULE = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_CART_SUBTITLE = (By.XPATH, '//*[@id="content_inner"]/p')