import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=ff_profile)
    else:
        print("Browser {} is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
