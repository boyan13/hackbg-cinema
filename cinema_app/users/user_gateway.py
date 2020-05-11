from ..db import Database
from ..db_shema.user import *
from ..db_shema.temp_table import *
from .models import UserModel




class UserGateway:
    def __init__(self):
        self.model = UserModel(id=None, email=None)
        self.db = Database()

    def create(self, *, email, password):
        user_data = (email, password)
        self.db.cursor.execute(CREATE_USER, user_data)
        u_id = self.get_user_id(email)
        self.db.cursor.execute(CREATE_CLIENT, (u_id,))
        self.db.connection.commit()

        # TODO: What whould I return?

    def get_user(self, *, email, password):
        query_args = (email, password)
        self.db.cursor.execute(FETCH_USER, query_args)
        user = self.db.cursor.fetchone()
        self.db.connection.commit()
        return user

    def set_temp_user(self, *, u_id, email):        
        self.db.cursor.execute(CREATE_TEMP_USER)
        self.db.cursor.execute(INSERT_TEMP_USER, (u_id, email))
        self.db.connection.commit()

    def del_temp_user(self):
        self.db.cursor.execute(DROP_TABLE)
        self.db.connection.commit()

    def get_user_id(self, email):
        self.db.cursor.execute(GET_USER_ID, (email,))
        user = self.db.cursor.fetchone()
        self.db.connection.commit()
        if user is not None:
            return user[0]
        return 0

def main():
    ugw = UserGateway()
    ugw.create(email="aaa@aa.a", password="12345AAA")


if __name__ == '__main__':
    main()
