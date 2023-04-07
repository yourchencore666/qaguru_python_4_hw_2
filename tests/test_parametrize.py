"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import be
from selene.support.shared import browser


@pytest.fixture(params=['Desktop', 'Mobile'])
def params_browser(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 540
        browser.config.window_height = 720
    yield
    browser.quit()


@pytest.mark.parametrize("params_browser", ["Desktop"], indirect=True)
def test_github_desktop(params_browser):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()


@pytest.mark.parametrize("params_browser", ["Mobile"], indirect=True)
def test_github_mobile(params_browser):
    browser.open("https://github.com/")
    browser.element("//button[@aria-label='Toggle navigation' and contains(@class,'Button')]").should(
        be.visible).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
