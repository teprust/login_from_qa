from faker import Faker
fake = Faker("ru_RU")


class LoginModel:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def random(self):
        username = fake.user_name()
        password = fake.password()
        return LoginModel(username=username, password=password)