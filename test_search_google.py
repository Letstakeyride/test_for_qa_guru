from selene.support.shared import browser
from selene import be, have


def test_successful_google_search(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_open_browser(conf_browser):
    browser.element('[name="q"]').should(be.blank).type('3213123123123123123214421312').press_enter()
    browser.element('[id = "result-stats"]').should(have.text("Результатов: примерно 0"))
