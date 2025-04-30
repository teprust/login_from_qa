import logging

from locators.login_locators import LoginLocators
from pages.base_page import BasePage

logger = logging.getLogger("qa")

class LoginPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_login_password(self, username_data, password_data):
        logger.info(f'Try to login with username {username_data}')
        logger.info(f'Try to login with password {password_data}')
        # Заполняем поле по локатору
        self.fill(value=username_data, locator=LoginLocators.USERNAME)
        self.fill(value=password_data, locator=LoginLocators.PASSWORD)

        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.LOGIN_BTN)

    def get_result_text(self):
        return self.text(LoginLocators.RESULT)

    def clean_form(self):
        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.RESET_BTN)
        logger.info('Clean form')