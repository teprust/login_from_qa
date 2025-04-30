import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_form import LoginPage
from pages.login_form_2 import LoginPage2


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/selenium-login-demo/", help="url")

@pytest.fixture(scope="session")
def login_page(request):

    # Настройка и открытие страницы
    url = request.config.getoption('--url')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get(url)

    # Экземпляр класса LoginForm
    login_page = LoginPage(driver)

    # yield алгоритм:
    # 1. передача экземпляра класса,
    # 2. выполнение действий вне данного метода,
    # 3. возврат к коду после yield.
    yield login_page
    driver.quit()

@pytest.fixture(scope="session")
def login_page_2(request):

    # Настройка и открытие страницы
    url = request.config.getoption('--url')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get(url)

    # Экземпляр класса LoginForm
    login_page = LoginPage2(driver)

    # yield алгоритм:
    # 1. передача экземпляра класса,
    # 2. выполнение действий вне данного метода,
    # 3. возврат к коду после yield.
    yield login_page
    driver.quit()