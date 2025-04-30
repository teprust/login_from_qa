from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, wait_time=10):
        '''
        Поиск элемента на веб-странице, с ожиданием загрузки (внутренний метод)
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время ожидания
        :return: возвращает объект selenium
        '''
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def click(self, locator, wait_time=10):
        '''
        Наажатие кнопки
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время ожидания
        '''
        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, value: str, locator, wait_time=60):
        '''
        fill = send_keys - т.е. заполнение текстового поля
        :param value: строка, которая будет добавлена в поле
        :param locator: аналогичен (By.ID, 'username')
        :param wait_time: время ожидания
        '''
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        '''

        :param locator:
        :param wait_time: аналогичен (By.ID, 'username')
        :return: текст ошибки (для нашего приложения - текст в поле вывода)
        '''
        element = self._find_element(locator, wait_time)
        return element.text()