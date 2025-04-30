import pytest

URL = "https://berpress.github.io/selenium-login-demo/"

@pytest.mark.skip
class TestLoginForm3:
    def test_happy_path(self, login_page):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        :return:
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page.add_login_password('admin', 'password')


    def test_unhappy_path_1(self, login_page):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        :return:
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page.add_login_password('adm', 'pass')



    def test_unhappy_path_2(self, login_page):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        :return:
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page.add_login_password('12345', '12345')
