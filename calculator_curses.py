import curses

def evaluate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Error"

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(False)
    stdscr.clear()

    expression = ""

    while True:
        stdscr.clear()

        # Draw calculator display
        stdscr.addstr(1, 2, " _____________________ ")
        stdscr.addstr(2, 2, "|  _________________  |")
        stdscr.addstr(3, 2, f"| |{expression[-17:]:>17}| |")
        stdscr.addstr(4, 2, "| |_________________| |")
        stdscr.addstr(5, 2, "|  ___ ___ ___   ___  |")
        stdscr.addstr(6, 2, "| | 7 | 8 | 9 | | / | |")
        stdscr.addstr(7, 2, "| |___|___|___| |___| |")
        stdscr.addstr(8, 2, "| | 4 | 5 | 6 | | * | |")
        stdscr.addstr(9, 2, "| |___|___|___| |___| |")
        stdscr.addstr(10,2, "| | 1 | 2 | 3 | | - | |")
        stdscr.addstr(11,2, "| |___|___|___| |___| |")
        stdscr.addstr(12,2, "| | 0 | . | = | | + | |")
        stdscr.addstr(13,2, "| |___|___|___| |___| |")
        stdscr.addstr(14,2, "| C - clear, Q - quit |")
        stdscr.addstr(15,2, "|_____________________|")

        stdscr.refresh()

        key = stdscr.getkey()

        if key in '0123456789+-*/.':
            expression += key
        elif key.lower() == 'c':
            expression = ""
        elif key == '\n':
            expression = evaluate_expression(expression)
        elif key.lower() == 'q':
            break

curses.wrapper(main)
