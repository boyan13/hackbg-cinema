import sys

from cinema_app.db import Database
from cinema_app.index_view import curses_main, user
from cinema_app.db_shema.temp_table import *
from cinema_app.db_shema.create_db import *
from cinema_app.users.user_gateway import UserGateway


class Application:
    @classmethod
    def build(self):
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
            UserGateway().del_temp_user()


    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
