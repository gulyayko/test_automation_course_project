from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_product_to_cart(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_cart_button()
#     page.add_to_cart()
#     page.product_added()
#     page.product_price()


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_cart(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.success_message_should_dissapear()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_is_empty()
    cart_page.empty_cart_subtitle()


