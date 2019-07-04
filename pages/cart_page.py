from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCTS_MODULE), "Cart is not empty"

    def empty_cart_subtitle(self):
        assert "Your basket is empty" in self.browser.find_element(*CartPageLocators.EMPTY_CART_SUBTITLE).text, \
            "Expected text for empty cart not present"
