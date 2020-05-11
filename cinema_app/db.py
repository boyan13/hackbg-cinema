import sqlite3

from .settings import DB_NAME

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        # print('Am closing meself')
