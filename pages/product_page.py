from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add to cart button is not presented"

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        self.solve_quiz_and_get_code()

    def product_added(self):
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        pass
        assert added_product, "Message about product added to the cart is not present"
        product_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert added_product.text == product_on_page.text, "Wrong product added"

    def product_price(self):
        cart_cost = self.browser.find_element(*ProductPageLocators.CART_COST).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert product_cost in cart_cost, "Wrong cart price"



