import curses


class Interface:
    def __init__(self, pos_x: int = 0, pos_y: int = 0):
        self.choosed_el = 0
        self.n = 3
        self.x = pos_x
        self.y = pos_y

    def update(self, key):
        if key == "Up":
            self.choosed_el -= 1
            if self.choosed_el < -1:
                self.choosed_el = self.n - 1

        if key == "Down":
            self.choosed_el += 1
            if self.choosed_el >= self.n:
                self.choosed_el = -1

    def choosed_field(self):
        if (self.choosed_el == self.n - 1):
            self.choosed_el -= 1
            return self.choosed_el + 1
        return self.choosed_el

    def draw_on(self, stdscr, mode):
        if mode:
            curses.start_color()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

            stdscr.addstr(0, 0, " _______")  # " _______"
            stdscr.addstr(1, 0, "|       |")  # "|       |"

            stdscr.addstr(2, 0, "|  ")  # "|  "
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(2, 3, "ON")  # "ON"
            stdscr.attroff(curses.color_pair(1))

            stdscr.addstr(2, 5, "   |")  # "   |"
            stdscr.addstr(3, 0, "|_______|")  # "|_______|"
        else:
            button = (" _______\n"
                      "|       |\n"
                      "|  ON   |\n"
                      "|_______|\n")
            stdscr.addstr(0, 0, button)

        stdscr.refresh()

    def display(self, stdscr, fields):
        if self.choosed_el == -1:
            self.draw_on(stdscr, True)
        else:
            self.draw_on(stdscr, False)

        for i, field in enumerate(fields):
            if self.choosed_el == i:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(i + 4 + self.y, self.x, f"{field}")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(i + 4 + self.y, self.x, field)
        # stdscr.addstr(10, 0, f"choosed_el: {self.choosed_el}    ")  #
        # stdscr.addstr(11, 0, f"self.n: {self.n}    ")               #
        stdscr.refresh()

    def change_n(self, n):
        self.n += n
