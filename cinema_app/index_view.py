import curses
import time

from .color_schemes import create_color_schemes
from .users.views import UserViews
# from .cinema.views import CinemaViews

account_options = ['Login', 'Sign in']
cinema_options = ['Make Reservation', 'Cancel Reservation', 'View Reservations', 'View Movies', 'Exit']
menu = account_options + cinema_options


def redirect(stdscr, string):
    user_views = UserViews()

    if string == menu[0]:
        user_views.login(stdscr)

    elif string == menu[1]:
        user_views.signin(stdscr)

    elif string == menu[2]:
        # make_res(stdscr)
        pass

    elif string == menu[3]:
        # cancel_res(stdscr)
        pass

    elif string == menu[4]:
        # view_res(stdscr)
        pass

    elif string == menu[5]:
        # view_movies(stdscr)
        pass

    else:
        raise ValueError


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    title = "Cinema System"
    stdscr.addstr(h // 2 - 5, w // 2 - len(title) // 2, title, curses.A_BOLD)

    for idx, row in enumerate(menu):
        if idx == 0 or idx == 1:
            x = w - len(row) - 2
            y = 1 + idx
        else:
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu) // 2 + idx

        # if idx in (2, 3, 4):

        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main_menu(stdscr):

    # Configs
    curses.curs_set(0)

    # Color Pairs
    create_color_schemes()

    # Menu
    selected_row = 0
    while 1:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        print_menu(stdscr, selected_row)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(menu) - 1:
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if selected_row == len(menu) - 1:
                stdscr.addstr(h // 2, w // 2 - 8, "Goodbye!")
                stdscr.refresh()
                time.sleep(1)
                break
            else:
                redirect(stdscr, menu[selected_row])
                break


def curses_main():
    curses.wrapper(main_menu)


if __name__ == '__main__':
    curses.wrapper(main_menu)
