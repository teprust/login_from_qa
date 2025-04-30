URL = "https://berpress.github.io/selenium-login-demo/"

class TestLoginForm4:
    def test_happy_path(self, login_page_2):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('admin', 'password')

        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Успешно! Вход выполнен." in result_text, "Ошибка входа, неверная пара логин/пароль!"


    def test_unhappy_path_1(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('adm', 'pass')
        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Пользователь авторизовался с несуществующей парой логин/пароль"


    def test_unhappy_path_2(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password('12345', '12345')
        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Пользователь авторизовался с несуществующей парой логин/пароль"
