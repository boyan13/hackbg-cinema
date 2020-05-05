import sqlite3

from queries import *
from settings import DB_NAME


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def create_db_tables(self):
        query_movies = '''
        CREATE TABLE IF NOT EXISTS  Movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        rating REAL NOT NULL DEFAULT 0 CHECK (rating BETWEEN 0 AND 10)
        );'''

        self.cursor.execute(query_movies)

        query_users = '''
        CREATE TABLE IF NOT EXISTS  User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(130) NOT NULL
        );
        '''

        self.cursor.execute(query_users)

        query_client = '''
        CREATE TABLE IF NOT EXISTS  Client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User(id)
        );
        '''

        self.cursor.execute(query_client)

        query_employee = '''
        CREATE TABLE IF NOT EXISTS  Empoyee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE NOT NULL,
        FOREIGN KEY (user_id) REFERENCES User(id)
        );
        '''

        self.cursor.execute(query_employee)

        query_projections = '''
        CREATE TABLE IF NOT EXISTS  Projections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER UNIQUE NOT NULL,
        type VARCHAR(5),
        date VARCHAR(10) NOT NULL,
        time VARCHAR(5) NOT NULL,
        FOREIGN KEY (movie_id) REFERENCES Movies(id)
        );
        '''

        self.cursor.execute(query_projections)

        query_reservations = '''
        CREATE TABLE IF NOT EXISTS  Reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        projection_id INTEGER NOT NULL,
        row INTEGER NOT NULL CHECK (row BETWEEN 1 AND 10),
        col INTEGER NOT NULL CHECK (col BETWEEN 1 AND 10),
        FOREIGN KEY (user_id) REFERENCES User(id),
        FOREIGN KEY (projection_id) REFERENCES Projection(id)
        );
        '''

        self.cursor.execute(query_reservations)

        self.connection.commit()

    def create_user(self, *, email, password):
        user_data = (email, password)
        query_create_user = '''
        INSERT INTO User (email, password)
        VALUES (?, ?);
        '''
        self.cursor.execute(query_create_user, user_data)

        id = self.get_user_id(email)

        query_create_client = '''
        INSERT INTO Client (user_id)
        VALUES (?);
        '''

        self.cursor.execute(query_create_client, (id,))
        self.connection.commit()

    def fetch_user(self, *, email, password):
        query_args = (email, password)
        self.cursor.execute(FETCH_USER, query_args)
        return self.cursor.fetchone()

    def get_user_id(self, email):
        query = '''SELECT id FROM User WHERE email = ?'''
        self.cursor.execute(query, (email,))
        user = self.cursor.fetchone()
        self.connection.commit()
        if user is not None:
            return user[0]
        return 0

    def __del__(self):
        self.connection.close()
        # print('Am closing meself')


def main():
    d = Database()
    d.create_db_tables()
    d.create_user(email="sisi@abv.bg", password="azAz1aaa")


if __name__ == '__main__':
    main()
