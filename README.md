# login_form_qa
### Автоматизированные UI-тесты с использованием Python и Selenium WebDriver для сайта авторизации

## План:
1. Написание тестов (15.1, 15.2)
2. Внедрение PageObject (15.1)
3. Добавить отчеты (15.2)
4. Интеграция с TMS (15.2)
5. Настройка CI/CD (15.2)
6. Описание проекта в Readme
7. Создание TestCases (один позитивный, два негативных) (15.1)

    7.1. Позитивный сценарий 1:  login=admin, password=password 

    7.2. Негативный сценарий 1:  login=adm, password=pass 

    7.3. Негативный сценарий 2:  login=12345, password=12345
8. Логгирование (15.2)
9. Pre-commit-hook (later)
10. Pytest (15.1)
11. Изучить тестируемое приложение (15.1)

    11.1. Форма состоит из двух полей - логин и пароль, двух кнопок - вход и очистить
12. Random и модели (15.2)

Тестируемое приложение: https://berpress.github.io/selenium-login-demo/

**How to start**

Use python 3.10 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

and start all tests

```
pytest
```