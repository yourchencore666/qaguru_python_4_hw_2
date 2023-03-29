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
@allure.story('Чистый Selene (без шагов)')
@allure.link(URL_GITHUB, name='Testing')
def test_search_github_issue():
    browser.open(URL_GITHUB)

    s('.header-search-input').click()
    s('.header-search-input').send_keys(REPO_NAME)
    s('.header-search-input').submit()

    s(by.link_text(REPO_NAME)).click()

    s('#issues-tab').click()

    s(by.partial_text(ISSUE_NUMBER)).should(be.visible)

    browser.quit()