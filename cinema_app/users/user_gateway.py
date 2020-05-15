from ..db import Database
from ..db_shema.user import *
from ..db_shema.temp_table import *
from .models import UserModel, ClientModel, Temp_user




class UserGateway:
    def __init__(self):
        self.model = UserModel()
        self.db = Database()

    def create(self, *, email, password):
        self.db.session.add_all([UserModel(email=email, password=password)])
        self.db.session.commit()
        u_id = self.db.session.query(UserModel.Id).filter(UserModel.email == email).first()
        self.db.session.add_all([ClientModel(user_id=u_id[0])])
        self.db.session.commit()

    def get_user(self, *, email, password):
        user = self.db.session.query(UserModel.Id, UserModel.email).filter(UserModel.email == email, UserModel.password == password).first()
        return user

    def set_temp_user(self, *, u_id, email): 
        self.db.Base.metadata.create_all(self.db.engine, tables=[Temp_user.__table__])
        self.db.session.add_all([Temp_user(email=email, user_id=u_id)])
        self.db.session.commit()

    def del_temp_user(self):
        Temp_user.__table__.drop(self.db.engine)

    def get_user_id(self, email):
        u_id = self.db.session.query(UserModel.Id).filter(UserModel.email == email).first()
        if u_id is not None:
            return u_id.Id
        return 0

def main():
    ugw = UserGateway()
    ugw.create(email="aaa@aa.a", password="12345AAA")


if __name__ == '__main__':
    main()
