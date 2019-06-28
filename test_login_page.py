from pages.login_page import LoginPage
from time import sleep

link = "http://selenium1py.pythonanywhere.com/accounts/login/"


def test_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
