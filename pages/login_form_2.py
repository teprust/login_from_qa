import logging

from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from pages.models.login_model import LoginModel

logger = logging.getLogger("qa")

class LoginPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_login_password(self, data: LoginModel):
        logger.info(f'Try to login with username {data.username}')
        logger.info(f'Try to login with password {data.password}')
        # Заполняем поле по локатору
        self.fill(value=data.username, locator=LoginLocators.USERNAME)
        self.fill(value=data.password, locator=LoginLocators.PASSWORD)

        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.LOGIN_BTN)

    def get_result_text(self):
        return self.text(LoginLocators.RESULT)

    def clean_form(self):
        # Нажатие на кнопку по локатору
        self.click(locator=LoginLocators.RESET_BTN)
        logger.info('Clean form')