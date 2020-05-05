#import sys
#sys.path.append(".")
from db import Database
from .models import UserModel
import hashlib
import re



class UserGateway:
    def __init__(self):
        self.model = UserModel(id=None, email=None)
        self.db = Database()

    @staticmethod
    def validate(email, password):
        count_at = email.count("@")
        count_point = email.count(".")

        if count_at != 1:
            raise Exception("Invalid email.")
        elif count_point != 1:
            raise Exception("Invalid email.")
        else:
            index_a = email.find("@")
            index_p = email.find(".")
            if index_a >= index_p - 1:
                raise Exception("Invalid email.")
            if index_a == 0 or index_p == len(email) - 1:
                raise Exception("Invalid email.")

        if len(password) < 8:
            raise Exception("Make sure your password is at lest 8 letters.")
        elif re.search('[0-9]', password) is None:
            raise Exception("Make sure your password has a number in it.")
        elif re.search('[A-Z]', password) is None:
            raise Exception("Make sure your password has a capital letter in it.")
        else:
            print("Your email and password are fine.")
            return True
        return False

    def make_it_secret(self, password):
        return hashlib.sha512(password.encode()).hexdigest()

    def create(self, *, email, password):
        UserGateway.validate(email, password)
        secret_password = self.make_it_secret(password)
        print(secret_password)
        print(len(secret_password))

        self.db.create_user(email=email, password=secret_password)

        # TODO: What whould I return?

    def set_user(self, *, email, password):
        hashpass = self.make_it_secret(password)
        raw_user = self.db.fetch_user(email=email, password=hashpass)

        if raw_user is None:
            raise RuntimeError("User not found.")
        else:
            user_id, user_email = raw_user
            self.model = UserModel(id=user_id, email=user_email)

    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]


def main():
    ugw = UserGateway()
    ugw.create(email="aaa@aa.a",password="a1Aaaaaaaaaaaaaaaaaaa")


if __name__ == '__main__':
    main()

