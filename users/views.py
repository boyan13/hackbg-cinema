from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        email = input('Email: ')
        password = input('Password: ')
        try:
            self.controller.set_user(email=email, password=password)
            print("Welcome, hacker.")
        except RuntimeError as e:
            print(str(e))

    def signup(self):
        email = input('Email: ')
        password = input('Password: ')
        try:
            self.controller.create_user(email=email, password=password)
        except Exception as e:
            print(str(e))
