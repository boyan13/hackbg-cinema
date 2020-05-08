import sqlite3

from .db_shema.queries import *
from .db_shema.temp_table import *
from .settings import DB_NAME

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def create_db_tables(self):
        self.cursor.execute(MOVIES)
        self.cursor.execute(USERS)
        self.cursor.execute(CLIENT)
        self.cursor.execute(EMPLOYEE)
        self.cursor.execute(PROJECTIONS)
        self.cursor.execute(RESERVATIONS)

        self.connection.commit()

    def create_user(self, *, email, password):
        user_data = (email, password)
        self.cursor.execute(CREATE_USER, user_data)

        id = self.get_user_id(email)

        self.cursor.execute(CREATE_CLIENT, (id,))
        self.connection.commit()

    def fetch_user(self, *, email, password):
        query_args = (email, password)
        self.cursor.execute(FETCH_USER, query_args)
        user = self.cursor.fetchone()
        self.connection.commit()
        return user

    def create_temp_user(self, *, id, email):
        self.cursor.execute(CREATE_TEMP_USER)
        self.cursor.execute(INSERT_TEMP_USER, (id, email))
        self.connection.commit()

    def get_temp_user(self):
        self.cursor.execute(GET_TEMP_USER)
        user = self.cursor.fetchone()
        self.connection.commit()
        return user

    def get_user_id(self, email):
        self.cursor.execute(GET_USER_ID, (email,))
        user = self.cursor.fetchone()
        self.connection.commit()
        if user is not None:
            return user[0]
        return 0

    def add_movies(self, *, title, rating):
        self.cursor.execute(ADD_MOVIE, (title, rating))
        self.connection.commit()

    def show_movies(self):
        self.cursor.execute(SHOW_MOVIES)
        movies = self.cursor.fetchall()
        self.connection.commit()
        # for m in movies:
        #     print("ID: {}, Title: {}, Rating: {}".format(m[0], m[1], m[2]))
        return movies

    def add_projection(self, *, date, time, movie_id, type):
        self.cursor.execute(ADD_PROJECTION, (movie_id, date, time, type))
        self.connection.commit()

    def show_all_projections(self, *, movie_id, order="ASC"):
        if order.upper() == "DESC":
            self.cursor.execute(SHOW_ALL_PROJECTIONS_D, (movie_id,))
        else:
            self.cursor.execute(SHOW_ALL_PROJECTIONS, (movie_id,))
        projections = self.cursor.fetchall()
        self.connection.commit()
        return projections

    def show_projections_date(self, *, movie_id, date):
        self.cursor.execute(SHOW_PROJECTIONS, (movie_id, date))
        projections = self.cursor.fetchall()
        self.connection.commit()
        return projections

    def make_reservation(self, *, user_id, projection_id, row, col):
        reservation_data = (user_id, projection_id, row, col)
        self.cursor.execute(MAKE_RESERVETION, reservation_data)
        self.connection.commit()

    def delete_reservation(self, *, user_id, projection_id, row, col):
        reservation_data = (user_id, projection_id, row, col)
        self.cursor.execute(DELETE_RESERVATION, reservation_data)
        self.connection.commit()

    def get_seats(self, *, projection_id):
        self.cursor.execute(GET_SEATS, (projection_id,))
        seats = self.cursor.fetchall()
        self.connection.commit()
        return seats

    def get_user_seats(self, *, projection_id, user_id):
        data = (projection_id, user_id)
        self.cursor.execute(GET_USER_SEATS, data)
        seats = self.cursor.fetchall()
        self.connection.commit()
        return seats

    def get_movie_by_id(self, movie_id):
        self.cursor.execute(GET_MOVIE_BY_ID, (movie_id,))
        movie = self.cursor.fetchone()
        self.connection.commit()
        return movie

    def all_projections(self):
        self.cursor.execute(GET_ALL_PROJECTIONS)
        pr = self.cursor.fetchall()
        self.connection.commit()
        return pr

    def get_user_reservation(self, id):
        self.cursor.execute(GET_USER_RESERVATIONS, (id,))
        r = self.cursor.fetchall()
        self.connection.commit()
        return r

    def del_temp_user(self):
        self.cursor.execute(DROP_TABLE)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
        #print('Am closing meself')


def main():
    d = Database()
    # d.create_db_tables()
    # d.create_user(email="sisi@abv.bg", password="azAz1aaa")
    # d.add_movies(title="Star wars VII", rating=8.5)
    # d.add_movies(title="Star wars IX", rating=8.7)
    # d.add_projection(movie_id=1, date="09-06-2020", time="13:45", type="3D")
    # movies = d.show_movies()
    # for m in movies:
    #     print("ID: {}, Title: {}, Rating: {}".format(m[0], m[1], m[2]))
    # projections = d.show_all_projections(movie_id=1)#, order="DESC")
    # print("Projections")
    # for p in projections:
    #     print("ID: {}, Date: {}, Time: {}, Type: {}, seats: {}".format(p[0], p[1], p[2], p[3], p[4]))
    # d.make_reservation(user_id=1,projection_id=1,row=4,col=5)
    # pr = d.show_projections_date(movie_id=1, date="2020-05-10")
    # for p in pr:
    #     print(p)
    # d.delete_reservation(user_id=1,projection_id=1,row=4,col=5)
    # pr = d.show_projections_date(movie_id=1, date="2020-05-10")
    # for p in pr:
    #     print(p)
    # print(d.get_seats(projection_id=1))


if __name__ == '__main__':
    main()
