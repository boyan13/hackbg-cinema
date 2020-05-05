import sys
sys.path.append(".")
from ..db import Database
from .models import UserModel
import hashlib


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def make_it_secret(self, password):
        return hashlib.sha512(password.encode()).hexdigest()

    def create(self, *, email, password):
        exc = None
        try:
            self.model.validate(email, password)
        except Exception as e:
            exc = e
            if exc is not None:
                print(exc)
        else:
            secret_password = self.make_it_secret(password)
            print(secret_password)
            print(len(secret_password))

        # self.db.cursor.execute()  # TODO: create user query

        # TODO: What whould I return?

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]


def main():
    ugw = UserGateway()
    ugw.create(email="aaa@aa.a",password="a1Aaaaaaaaaaaaaaaaaaa")


if __name__ == '__main__':
    main()
