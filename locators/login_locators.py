from selenium.webdriver.common.by import By

class LoginLocators:
    '''
    Идентификаторы элементов формы:
        Логин - id=username
        Пароль - id=password
        Вход - id=login-btn
        Очистить - id=reset-btn
        Результат - id=result
    '''

    # Описываем локаторы
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-btn')
    RESET_BTN = (By.ID, 'reset-btn')
    RESULT = (By.ID, 'result')