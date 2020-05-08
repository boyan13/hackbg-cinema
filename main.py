import sys

from cinema_app.db import Database
from cinema_app.index_view import curses_main, user


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.create_db_tables()

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
            db.del_temp_user()


    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
