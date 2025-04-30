URL = "https://berpress.github.io/selenium-login-demo/"

class TestLoginForm4:
    def test_happy_path(self, login_page_2):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('admin', 'password')


    def test_unhappy_path_1(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('adm', 'pass')



    def test_unhappy_path_2(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('12345', '12345')
