import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

URL_GITHUB = 'https://github.com'
REPO_NAME = 'yourchencore666/qaguru_python_4_hw_2'
ISSUE_NUMBER = '#8'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'yurchenko_a')
@allure.feature(f'Проверка наличия Issue {ISSUE_NUMBER} на github')
@allure.story('Шаги с декоратором @allure.step')
@allure.link(URL_GITHUB, name='Testing')
def test_search_github_issue():
    open_main_page(URL_GITHUB)
    search_for_repository(REPO_NAME)
    go_to_repository(REPO_NAME)
    open_issue_tab()
    should_see_issue_with_number(ISSUE_NUMBER)
    browser.quit()


@allure.step('Открываем главную страницу')
def open_main_page(url):
    browser.open(url)


@allure.step(f'Поиск репозитория {REPO_NAME}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step(f'Переход по ссылке репозитория {REPO_NAME}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открытие tab Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step(f'Проверка наличие Issue с номером {ISSUE_NUMBER}')
def should_see_issue_with_number(issue_number):
    s(by.partial_text(issue_number)).should(be.visible)