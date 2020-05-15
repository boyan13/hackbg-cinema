import curses
import curses.textpad
from .controllers import UserContoller
from .models import login_exceptions, signin_exceptions


class UserViews:

    def __init__(self):
        self.controller = UserContoller()
        self.login_exceptions = login_exceptions
        self.signin_exceptions = signin_exceptions

    def retry_dialogue(self, stdscr, message):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        selected_col = 0
        while 1:
            stdscr.addstr(h // 2 - 4, w // 2 - len(message) // 2, message)

            if selected_col == 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(h // 2, w // 2 - len("Cancel") // 2 - 10, "Cancel")
                stdscr.attroff(curses.color_pair(1))
                stdscr.addstr(h // 2, w // 2 + len("Retry") // 2 + 10, "Retry")
            elif selected_col == 1:
                stdscr.addstr(h // 2, w // 2 - len("Cancel") // 2 - 10, "Cancel")
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(h // 2, w // 2 + len("Retry") // 2 + 10, "Retry")
                stdscr.attroff(curses.color_pair(1))

            stdscr.refresh()
            key = stdscr.getch()
            stdscr.clear()

            if key == curses.KEY_LEFT and selected_col == 1:
                selected_col = 0
            elif key == curses.KEY_RIGHT and selected_col == 0:
                selected_col = 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if selected_col == 0:
                    return False
                elif selected_col == 1:
                    return True

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
        try:
            self.controller.get_user(email=e, password=p)
        except Exception as exc:
            if str(exc) not in self.login_exceptions:
                raise
            else:
                if self.retry_dialogue(stdscr, str(exc)):
                    self.login(stdscr)
                else:
                    return

    def signin(self, stdscr):
        stdscr.clear()
        e, p = self.account_form(stdscr, "Sign in")
        stdscr.clear()

        try:
            self.controller.create_user(email=e, password=p)
        except Exception as exc:
            if str(exc) not in self.signin_exceptions:
                raise
            else:
                if self.retry_dialogue(stdscr, str(exc)):
                    self.signin(stdscr)
                else:
                    return


if __name__ == '__main__':
    curses.wrapper(login)
