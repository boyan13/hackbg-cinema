# Internal Imports
from .user_gateway import UserGateway

# STD Library Imports
import hashlib
import time


class UserContoller:
    def __init__(self):
        self.user_gateway = UserGateway()

    def make_it_secret(self, password):
        return hashlib.sha512(password.encode()).hexdigest()

    def create_user(self, email, password):
        self.user_gateway.model.validate(email, password)
        hashpass = self.make_it_secret(password)
        self.user_gateway.create(email=email, password=hashpass)
        # self.get_user(email=email, password=password)

        # send email
        # sync with Slack

    def get_user(self, *, email, password):
        hashpass = self.make_it_secret(password)
        raw_user = self.user_gateway.get_user(email=email, password=hashpass)
        if raw_user is None:
            raise Exception("User not found.")
        else:
            self.user_gateway.set_temp_user(u_id=raw_user[0], email=raw_user[1])
            # TODO temp Table User_t return raw_user
            pass


    def del_temp_user(self):
        self.user_gateway.del_temp_user()
