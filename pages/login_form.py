from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def add_login_password(self, username_data, password_data):
        '''
        1. Поиск идентификаторов элементов формы
            Логин - id=username
            Пароль - id=password
            Вход - id=login-btn
            Очистить - id=reset-btn
        '''

        # Поиск элементов
        username = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        login_btn = self.driver.find_element(By.ID, 'login-btn')
        reset_btn = self.driver.find_element(By.ID, 'reset-btn')

        # Взаимодействие с элементами формы по id
        username.send_keys(username_data)
        password.send_keys(password_data)
        login_btn.click()
        reset_btn.click()