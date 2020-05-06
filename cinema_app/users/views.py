import curses
import curses.textpad
import time


def get_reg_info(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    dialogue = "Fill in account detail below: WARNING THIS FILE IS WIP!"
    dialogue_width = w // 2 - len(dialogue) // 2

    stdscr.addstr(h // 3, dialogue_width, dialogue)

    email_win = curses.newwin(1, 50, h // 3 + 2, 2)
    curses.textpad.rectangle(stdscr, h // 3 + 1, 1, h // 3 + 1 + 1 + 1, 1 + 50 + 1)

    password_win = curses.newwin(1, 50, h // 3 + 2, 55)
    curses.textpad.rectangle(stdscr, h // 3 + 1, 55, h // 3 + 1 + 1 + 1, 55 + 50 + 1)

    stdscr.refresh()

    email_box = curses.textpad.Textbox(email_win)
    email_box.edit()
    email = email_box.gather()

    # stdscr.clear()
    # # height, width, top left (y), top right (x)
    # win = curses.newwin(5, 30, 2, 1)
    # # window, top left (y), top left (x), bottom right (y), bottom right (x)
    # curses.textpad.rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)
    # stdscr.refresh()

    # box = curses.textpad.Textbox(win)

    # box.edit()

    # message = box.gather()

    # stdscr.clear()
    # stdscr.addstr(message)
    # stdscr.refresh()
    # time.sleep(10)


if __name__ == '__main__':
    curses.wrapper(get_reg_info)
