from pages.models.login_model import LoginModel


class TestLoginForm4:
    def test_happy_path(self, login_page_2):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        '''

        data = LoginModel('admin', 'password')

        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password(data=data)

        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Успешно! Вход выполнен." in result_text, "Ошибка входа, неверная пара логин/пароль!"


    def test_unhappy_path_1(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        data = LoginModel('adm', 'pass')
        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password(data=data)
        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Пользователь авторизовался с несуществующей парой логин/пароль"


    def test_unhappy_path_2(self, login_page_2):
        '''
        1. Вводим некорректные данные
        2. Проверяем результат
        '''

        data = LoginModel('12345', '12345')
        # Метод поиска элементов на форме и взаимодействия с ними
        login_page_2.add_login_password(data=data)
        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        assert "Ошибка: Неверный логин или пароль." in result_text, "Пользователь авторизовался с несуществующей парой логин/пароль"

    def test_random_user(self, login_page_2):
        '''
        1. Вводим некорректные рандомные данные
        2. Проверяем результат
        '''

        # Метод поиска элементов на форме и взаимодействия с ними
        data = LoginModel().random()
        login_page_2.add_login_password(data=data)
        result_text = login_page_2.get_result_text()
        login_page_2.clean_form()
        if data.username == 'admin' and data.password == 'password':
            assert "Успешно! Вход выполнен." in result_text, "Ошибка входа, неверная пара логин/пароль!"
        else:
            assert "Ошибка: Неверный логин или пароль." in result_text, "Пользователь авторизовался с несуществующей парой логин/пароль"