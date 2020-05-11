import sys

from cinema_app.db import Database
from cinema_app.index_view import curses_main, user
from cinema_app.db_shema.temp_table import *
from cinema_app.db_shema.create_db import *


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(MOVIES)
        db.cursor.execute(USERS)
        db.cursor.execute(CLIENT)
        db.cursor.execute(EMPLOYEE)
        db.cursor.execute(PROJECTIONS)
        db.cursor.execute(RESERVATIONS)

        db.connection.commit()

        print('Done.')

    @classmethod
    def start(self):
        curses_main()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        try:
            Application.start()
        except Exception as exc:
            raise
        finally:
            db = Database()
            db.cursor.execute(DROP_TABLE)
            db.connection.commit()


    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
