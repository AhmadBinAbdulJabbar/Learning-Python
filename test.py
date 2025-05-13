import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0, "Hello, World!")
    stdscr.addstr(1, 0, "Press any key to exit.")

    stdscr.move(4, 0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.addstr("Red Text", curses.color_pair(1))

    # stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)