import re


class UserModel:
    def __init__(self, *, id, email):
        self.id = id
        self.email = email

    @staticmethod
    def validate(email):
        pass


def main():
    UserModel.validate("AZ@abv.bg")


if __name__ == '__main__':
    main()
