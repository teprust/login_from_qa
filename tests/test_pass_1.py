import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://berpress.github.io/selenium-login-demo/"

'''
1. Поиск идентификаторов элементов формы 
    Логин - id=username
    Пароль - id=password
    Вход - id=login-btn
    Очистить - id=reset-btn 
'''
@pytest.mark.skip
class TestLoginForm1:
    def test_happy_path(self):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Поиск элементов
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_btn = driver.find_element(By.ID, 'login-btn')
        reset_btn = driver.find_element(By.ID, 'reset-btn')

        # Взаимодействие с элементами формы по id
        username.send_keys('admin')
        password.send_keys('password')
        login_btn.click()

        driver.quit()

    def test_unhappy_path_1(self):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Поиск элементов
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_btn = driver.find_element(By.ID, 'login-btn')
        reset_btn = driver.find_element(By.ID, 'reset-btn')

        # Взаимодействие с элементами формы по id
        username.send_keys('adm')
        password.send_keys('pass')
        login_btn.click()

        driver.quit()

    def test_unhappy_path_2(self):
        '''
        1. Вводим корректные данные
        2. Проверяем результат
        :return:
        '''

        # Открытие страницы
        driver = webdriver.Chrome()
        driver.get(URL)

        # Поиск элементов
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        login_btn = driver.find_element(By.ID, 'login-btn')
        reset_btn = driver.find_element(By.ID, 'reset-btn')

        # Взаимодействие с элементами формы по id
        username.send_keys('12345')
        password.send_keys('12345')
        login_btn.click()

        driver.quit()