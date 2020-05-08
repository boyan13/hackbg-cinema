import curses
import curses.textpad
from .controllers import UserContoller


class UserViews:

    def __init__(self):
        self.controller = UserContoller()

    def account_form(self, stdscr, form_title):
        stdscr.clear()
        curses.curs_set(1)
        try:
            h, w = stdscr.getmaxyx()

            stdscr.addstr(h // 2 - 6, 5, form_title, curses.A_BOLD)
            dialogue = "Fill in account detail below:"
            stdscr.addstr(h // 2 - 3, 5, dialogue)

            email_win = curses.newwin(1, 50, h//2, 5)
            curses.textpad.rectangle(stdscr, h//2 -1, 5 -1, h//2 -1 +1+1, 5 -1 +50 +1)
            curses.textpad.rectangle(stdscr, h//2+3 -1, 5 -1, h//2+3 -1 +1+1, 5 -1 +50 +1)
            stdscr.refresh()

            # Get email via textbox
            email_box = curses.textpad.Textbox(email_win)
            email_box.edit()
            email = email_box.gather()

            # Get password via getch and simulated cursor
            display = str()
            password = str()

            line_start_y = h // 2 + 3
            line_start_x = 5
            cursor_movement_x = line_start_x

            stdscr.clear()
            while 1:
                stdscr.addstr(h // 2 - 6, 5, form_title, curses.A_BOLD)
                dialogue = "Fill in account detail below:"
                stdscr.addstr(h // 2 - 3, 5, dialogue)

                curses.textpad.rectangle(stdscr, h//2 -1, 5 -1, h//2 -1 +1+1, 5 -1 +50 +1)
                stdscr.addstr(h // 2, 5, email)
                curses.textpad.rectangle(stdscr, h//2+3 -1, 5 -1, h//2+3 -1 +1+1, 5 -1 +50 +1)
                stdscr.move(line_start_y, cursor_movement_x)
                key = stdscr.getch()
                stdscr.clear()

                if key == curses.KEY_ENTER or key in [10, 13]:
                    break

                if key == curses.KEY_DC or key == curses.KEY_BACKSPACE or key == 127:
                    if len(display) > 0:
                        display = display[:-1]
                    if cursor_movement_x > 0:
                        cursor_movement_x -= 1
                    if len(password) > 0:
                        password = password[:-1]

                else:
                    display += '*'
                    cursor_movement_x += 1
                    password += chr(key)

                stdscr.addstr(line_start_y, line_start_x, display)
                stdscr.refresh()
        finally:
            curses.curs_set(0)

        return (email, password)

    def login(self, stdscr):
        stdscr.clear()
        e, p = self.account_form(stdscr, "Login")
        stdscr.clear()

        self.controller.get_user(email=e, password=p)

    def signin(self, stdscr):
        stdscr.clear()
        e, p = self.account_form(stdscr, "Sign in")
        stdscr.clear()

        self.controller.create_user(email=e, password=p)


if __name__ == '__main__':
    curses.wrapper(login)
