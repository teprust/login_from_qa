from selenium.webdriver.common.by import By

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_login_password(self, username_data, password_data):

        # Заполняем поле по локатору
        self.fill(value=username_data, locator=LoginLocators.USERNAME)
        self.fill(value=password_data, locator=LoginLocators.PASSWORD)

        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.LOGIN_BTN)
        self.click(locator=LoginLocators.RESET_BTN)
