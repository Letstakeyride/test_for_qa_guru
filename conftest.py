import pytest
from selene.support.shared import browser, config
from selene import be, have


@pytest.fixture(scope="function")
def conf_browser():
    browser.open('https://google.com')
    browser.driver.maximize_window()