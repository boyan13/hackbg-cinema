import sys

from cinema_app.db import Database
from cinema_app.index_view import curses_main


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.create_db_tables()
        db.close()

        print('Done.')

    @classmethod
    def start(self):
        curses_main()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
