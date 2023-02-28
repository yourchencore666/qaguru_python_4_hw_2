import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def config_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 768

def test_google_find_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_find_negative_naming():

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kakyatopolnayachepuha').press_enter()
    browser.element('.card-section').should(have.text('По запросу kakyatopolnayachepuha ничего не найдено.'))