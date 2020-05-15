from ..db import Database
from .movie_model import MovieModel
from ..users.models import Temp_user


class MovieGateway:
    def __init__(self):
        self.model = MovieModel()
        self.db = Database()

    def get_movies(self):
        movies = self.db.session.query(MovieModel.Id, MovieModel.name, MovieModel.rating).all()
        self.db.session.commit()
        return movies

    def get_movie(self, movie_id):
        movie = self.db.session.query(MovieModel.Id, MovieModel.name, MovieModel.rating).filter(MovieModel.Id == movie_id).first()
        self.db.session.commit()
        return movie



    def get_user_id(self):
        u_id = self.db.session.query(Temp_user.Id).first()
        self.db.session.commit()
        return u_id[0]
        # self.db.cursor.execute(GET_TEMP_USER)
        # user = self.db.cursor.fetchone()
        # self.db.connection.commit()
        # return user[0]

    def get_user_info(self):
        user = self.db.session.query(Temp_user.Id, Temp_user.email).first()
        self.db.session.commit()
        return user
        # self.db.cursor.execute(GET_TEMP_USER)
        # user = self.db.cursor.fetchone()
        # self.db.connection.commit()
        # return user

