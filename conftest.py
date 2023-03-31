import os
import zipfile
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

current_dir = os.path.dirname(os.path.abspath(__file__))
resources = os.path.join(current_dir, "tests/resources")


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = False
    browser.config.base_url = 'https://demoqa.com'


@pytest.fixture
def setup_chrome(request):
    browser_name = request.config.getoption('--browser')
    options = Options()
    options.add_argument("--window-size=1920,1080")

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver


@pytest.fixture
def create_zip():
    file_list = []
    for filename in os.listdir(resources):
        file_list.append(filename)

    with zipfile.ZipFile("resources/archive.zip", 'w') as filezip:
        for filename in file_list:
            filezip.write(f"resources/{filename}", filename)


@pytest.fixture
def delete_zip():
    yield
    path = f"{resources}/archive.zip"
    os.remove(path)
    print("zipfile is deleted")
