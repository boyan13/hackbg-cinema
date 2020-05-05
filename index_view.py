import curses
import time


menu = ['Login', 'Sign in', 'View Movies', 'Exit']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
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

    # Configs
    curses.curs_set(0)

    # Color Pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Menu
    selected_row = 0
    while 1:
        stdscr.clear()
        print_menu(stdscr, selected_row)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(menu) - 1:
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if selected_row == len(menu) - 1:
                stdscr.addstr("Goodbye!")
                stdscr.refresh()
                time.sleep(1)
                break
            else:
                # TODO parse(menu[selected_row])
                stdscr.addstr(f"You chose {menu[selected_row]}")
                stdscr.refresh()
                time.sleep(3)
                break


def curses_main():
    curses.wrapper(main_menu)

if __name__ == '__main__':
    curses.wrapper(main_menu)
