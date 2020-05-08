import curses
import time

from .color_schemes import create_color_schemes
from .users.views import UserViews
from .cinema.views import CinemaViews
from .cinema.controllers import CinemaController

registration_options = ['Login', 'Sign in']
user_options = ['Make Reservation', 'Cancel Reservation', 'View Reservations']  # Must be logged in
public_options = ['View Porgram', 'View Movies', 'Exit']
menu = registration_options + user_options + public_options  # The order is important for indexing!!!


def redirect(stdscr, string):
    user_views = UserViews()
    cinema_views = CinemaViews()

    if string == menu[0]:
        user_views.login(stdscr)

    elif string == menu[1]:
        user_views.signin(stdscr)

    elif string == menu[2]:
        curses.endwin()
        cinema_views.make_reservation()

    elif string == menu[3]:
        curses.endwin()
        cinema_views.cancel_reservation()

    elif string == menu[4]:
        curses.endwin()
        cinema_views.print_reservations()

    elif string == menu[5]:
        curses.endwin()
        cinema_views.print_program()

    elif string == menu[6]:
        curses.endwin()
        cinema_views.print_movies()

    else:
        raise ValueError

    main_menu(stdscr)

def display_menu(stdscr, selected_row_idx, first_row):
    h, w = stdscr.getmaxyx()

    title = "Cinema System"
    stdscr.addstr(h // 2 - 5, w // 2 - len(title) // 2, title, curses.A_BOLD)

    for idx in range(first_row, len(menu)):
        row = menu[idx]

        if idx in [0, 1]:
            x = w - len(row) - 2
            y = 1 + idx
        else:
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu) // 2 + idx

        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main_menu(stdscr):
    stdscr.clear()

    # Color Pairs
    create_color_schemes()

    # Configs
    curses.curs_set(0)

    cinema_controller = CinemaController()

    logged = True
    try:
        u = cinema_controller.get_user_info()
    except Exception as exc:
        if str(exc) == "First login!":
            logged = False
        else:
            raise

    if logged:
        selected_row = 2
        first_row = 2
    else:
        selected_row = 0
        first_row = 0

    while 1:
        h, w = stdscr.getmaxyx()

        if logged:
            stdscr.addstr(1, w - len(u[1]) - 2, u[1])

        display_menu(stdscr, selected_row, first_row)
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and selected_row > first_row:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(menu) - 1:
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if selected_row == len(menu) - 1:
                stdscr.addstr(h // 2, w // 2 - 8, "Goodbye!")
                stdscr.refresh()
                time.sleep(1)
                exit()

            elif selected_row in [2, 3, 4]:
                if logged:
                    redirect(stdscr, menu[selected_row])
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(h - 3, w // 2 - 11, "You must login first!")
                    stdscr.attroff(curses.color_pair(2))
                    stdscr.refresh()

            else:
                redirect(stdscr, menu[selected_row])


def user():
    cinema = CinemaController()
    return cinema.get_user_info()

def curses_main():
    curses.wrapper(main_menu)


if __name__ == '__main__':
    curses.wrapper(main_menu)
