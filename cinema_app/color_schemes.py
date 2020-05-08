import curses


def create_color_schemes():
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Select Option
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Error
