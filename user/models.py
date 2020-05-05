import re


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        pass


def main():
    UserModel.validate("AZ@abv.bg", "12345Aaa")


if __name__ == '__main__':
    main()
