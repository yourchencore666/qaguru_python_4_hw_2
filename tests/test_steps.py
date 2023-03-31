import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

from selene.support.shared.jquery_style import s


from demoqa_tests import helpers

URL_GITHUB = 'https://github.com'
REPO_NAME = 'yourchencore666/qaguru_python_4_hw_2'
ISSUE_NUMBER = '#8'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'yurchenko_a')
@allure.feature(f'Проверка наличия Issue {ISSUE_NUMBER} на github')
@allure.story('Лямбда шаги через with allure.step')
@allure.link(URL_GITHUB, name='Testing')
def test_search_github_issue(setup_chrome):
    with allure.step('Открываем главную страницу'):
        browser.open(URL_GITHUB)

    with allure.step(f'Поиск репозитория {REPO_NAME}'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys(REPO_NAME)
        s('.header-search-input').submit()

    with allure.step(f'Переход по ссылке репозитория {REPO_NAME}'):
        s(by.link_text(REPO_NAME)).click()

    with allure.step('Открытие tab Issues'):
        s('#issues-tab').click()

    with allure.step(f'Проверка наличие Issue с номером {ISSUE_NUMBER}'):
        s(by.partial_text(ISSUE_NUMBER)).should(be.visible)

    helpers.add_logs(browser)
    helpers.add_screenshot(browser)
    helpers.add_html(browser)
    helpers.add_video(browser)

    browser.quit()
