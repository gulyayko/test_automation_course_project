import pytest

"""please do not forget to import this module into venv of the project by using requirements.txt file
or by install mimesis with command "pip install mimesis"
"""
from mimesis import Person

from pages import CartPage
from pages import LoginPage
from pages import ProductPage

person = Person('en')

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                       marks=pytest.mark.xfail(reason="should fail")),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.product_added()
    page.product_price()


@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(person.email(domains=["@fakemail.org"]), person.password(9))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_to_cart()
        page.product_added()
        page.product_price()


@pytest.mark.xfail(reason="Test intentionally fails for educational purposes.")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Test intentionally fails for educational purposes.")
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_cart()
    page.success_message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_is_empty()
    cart_page.empty_cart_subtitle()
