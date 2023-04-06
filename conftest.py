import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def conf_browser():
    browser.open('https://google.com')
    browser.driver.maximize_window()
