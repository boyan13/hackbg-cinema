from ..db import Database
from .movie_model import MovieModel
from ..db_shema.temp_table import *
from ..db_shema.movie import *


class MovieGateway:
    def __init__(self):
        self.model = MovieModel(m_id=None, name=None, rating=None)
        self.db = Database()

    def get_movies(self):
        self.db.cursor.execute(SHOW_MOVIES)
        movies = self.db.cursor.fetchall()
        self.db.connection.commit()
        return movies

    def get_movie(self, movie_id):
        self.db.cursor.execute(GET_MOVIE_BY_ID, (movie_id,))
        movie = self.db.cursor.fetchone()
        self.db.connection.commit()
        return movie



    def get_user_id(self):
        self.db.cursor.execute(GET_TEMP_USER)
        user = self.db.cursor.fetchone()
        self.db.connection.commit()
        return user[0]

    def get_user_info(self):
        self.db.cursor.execute(GET_TEMP_USER)
        user = self.db.cursor.fetchone()
        self.db.connection.commit()
        return user

