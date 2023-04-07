"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
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
    yield request.param
    browser.quit()


def test_github_desktop(params_browser):
    if params_browser == 'Desktop':
        browser.open("https://github.com/")
        browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    elif params_browser == 'Mobile':
        pytest.skip("Error browser type")



def test_github_mobile(params_browser):
    if params_browser == "Mobile":
        browser.open("https://github.com/")
        browser.element("//button[@aria-label='Toggle navigation' and contains(@class,'Button')]").should(
            be.visible).click()
        browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    else:
        pytest.skip("Error on browser type")
