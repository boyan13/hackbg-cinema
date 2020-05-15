# Internal Imports
from ..db import Database

# STD Library Imports
import re

# Third-Party Library Imports
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


db = Database()
signin_exceptions = ["Invalid email.", "Make sure your password is at lest 8 letters.", "Make sure your password has a number in it.", "Make sure your password has a capital letter in it."]
login_exceptions = ["User not found."]


class UserModel(db.Base):
    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

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
            # print("Your email and password are fine.")
            return True
        return False


class ClientModel(db.Base):
    __tablename__ = "Clients"
    Id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.Id"))
    user = relationship("UserModel", backref="Clients")


class Temp_user(db.Base):
    __tablename__ = "temp_user"
    Id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Clients.Id"))
    email = Column(String)
    temp_user = relationship("ClientModel", backref="temp_user")


# def main():
#     UserModel.validate("AZ@abv.bg")


# if __name__ == '__main__':
#     main()
