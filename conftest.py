import os
import zipfile
import pytest
from selene.support.shared import browser

@pytest.fixture
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = True
    browser.config.base_url = 'https://demoqa.com'


@pytest.fixture
def create_zip():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    resources = os.path.join(current_dir, "tests/resources")
    file_list = []
    for filename in os.listdir(resources):
        file_list.append(filename)

    with zipfile.ZipFile("resources/archive.zip", 'w') as filezip:
        for filename in file_list:
            filezip.write(f"resources/{filename}", filename)

@pytest.fixture
def delete_zip():
    yield
    path = "/Users/urcenkoartem/Documents/qaguru_python_4_hw_2/tests/resources/archive.zip"
    os.remove(path)
    print("zipfile is deleted")