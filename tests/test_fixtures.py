"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import be
from selene.support.shared import browser


@pytest.fixture
def desktop_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = False


@pytest.fixture
def mobile_browser():
    browser.config.window_width = 540
    browser.config.window_height = 720
    browser.config.hold_browser_open = False


def test_github_desktop(desktop_browser):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()

def test_github_mobile(mobile_browser):
    browser.open("https://github.com/")
    browser.element("//button[@aria-label='Toggle navigation' and contains(@class,'Button')]").should(be.visible).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()