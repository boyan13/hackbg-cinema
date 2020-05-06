from ..db import Database
from .models import MovieModel


class CinemaGateway:
    def __init__(self):
        self.model = MovieModel(id=None, name=None, rating=None)
        self.db = Database()

    def get_movies(self):
        return self.db.show_movies()

    def get_movie(self, id):
        return self.db.get_movie_by_id(id)

    def get_all_projections(self, *, movie_id, order):
        return self.db.show_all_projections(movie_id=movie_id, order=order)

    def get_projections_by_date(set, *, movie_id, date):
        return self.db.show_projections_date(movie_id=movie_id, date=date)

    def get_seats(self, projecton_id):
        return self.db.get_seats(projection_id=projection_id)

    def delete_reservation(self, *, id, projection_id, row, col):
        self.db.delete_reservation(user_id=id, projection_id=projection_id, row=row, col=col)

    def insert_reservation(self, *, id, projection_id, row, col):
        self.db.make_reservation(user_id=id, projection_id=projection_id, row=row, col=col)

    def get_user_seats(self, *, id, projection_id):
        return self.db.get_user_seats(user_id=id, projection_id=projection_id)

    def get_user_id(self):
        id = self.db.get_temp_user()
        return id[0]

    def get_user_info(self):
        return self.db.get_temp_user()
    # def get_resurved_seats(self, projection_id):
    #     return self.db.get_seats(projection_id=projection_id)
