#import sys
#sys.path.append(".")
from ..db import Database
from .models import UserModel




class UserGateway:
    def __init__(self):
        self.model = UserModel(id=None, email=None)
        self.db = Database()



    def create(self, *, email, password):
        self.db.create_user(email=email, password=password)

        # TODO: What whould I return?

    def get_user(self, *, email, password):
        return self.db.fetch_user(email=email, password=password)

    def set_temp_user(self, *, id, email):
        self.db.create_temp_user(id=id, email=email)

    """
    def get_movies(self):
        return self.db.show_movies()

    def get_projectons(self, *, movie_id, order):
        movie = self.db.get_movie_by_id(movie_id)
        if movie is None:
            raise Exception("Movie is not found.")
        return self.db.show_all_projections(movie_id=movie_id, order=order)
    
    def get_projectons_by_date(self, *, movie_id, date):
        movie = self.db.get_movie_by_id(movie_id)
        if movie is None:
            raise Exception("Movie is not found.")
        pr = self.db.show_projections_date(movie_id=movie_id, date=date)
        if pr is None:
            raise Exception("No projections.")
        return pr

    def show_seats(self, projection_id):
        return self.db.get_seats(projection_id=projection_id)

    def return_reserved_seats(self, projection_id):
        return self.db.get_seats(projection_id=projection_id)
    

    def insert_reservation(self, *, projection_id, row, col):
        if self.model.id is not None:
            self.db.make_reservation(user_id=self.model.id, projection_id=projection_id, row=row, col=col)

    def delete_reservation(self, *, projection_id, row, col):
        if self.model.id is None:
            self.db.delete_reservation(user_id=self.model.id, projection_id=projection_id, row=row, col=col)
    
    def get_user_seats(self, *, projection_id):
        if self.model.id is not None:
            return self.db.get_user_seats(user_id=self.model.id, projection_id=projection_id)
    """
    def all(self):
        raw_users = self.db.cursor.execute()  # TODO: Select all users

        return [self.model(**row) for row in raw_users]


def main():
    ugw = UserGateway()
    ugw.create(email="aaa@aa.a", password="12345AAA")


if __name__ == '__main__':
    main()
