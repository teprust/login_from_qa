from selenium import webdriver
from pages.login_form import LoginForm

URL = "https://berpress.github.io/selenium-login-demo/"



class TestLoginForm2:
    def test_happy_path(self):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Экземпляр класса LoginForm
        login_form = LoginForm(driver)

        # Метод поиска элементов на форме и взаимодействия с ними
        login_form.add_login_password('admin', 'password')

        driver.quit()

    def test_unhappy_path_1(self):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Экземпляр класса LoginForm
        login_form = LoginForm(driver)

        # Метод поиска элементов на форме и взаимодействия с ними
        login_form.add_login_password('adm', 'pass')

        driver.quit()

    def test_unhappy_path_2(self):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Экземпляр класса LoginForm
        login_form = LoginForm(driver)

        # Метод поиска элементов на форме и взаимодействия с ними
        login_form.add_login_password('12345', '12345')

        driver.quit()