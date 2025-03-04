import curses # noqa F401
from Keyboard.Key import Key


class Mouse:
    def __init__(self):
        self.status = False
        self.left_button = Key("Left Click")
        self.right_button = Key("Right Click")
        self.middle_button = Key("Middle Click")
        self.position = (0, 0)  # (x, y)

    @property
    def get_picture(self):
        picture = [
            '#' * 9,
            '#' + ' ' * 7 + '#',
            '#' + ' ' + '|' + ' ' * 3 + '|' + ' ' + '#',
            '#' + ' ' * 3 + '*' + ' ' * 3 + '#',
            '#' + ' ' * 3 + '*' + ' ' * 3 + '#',
            '#' + ' ' * 7 + '#',
            '#' + ' ' * 7 + '#',
            '#' + ' ' * 7 + '#',
            '#' + ' ' * 7 + '#',
            '#' * 9
        ]
        return picture

    def draw_mouse(self, stdscr, pos_x, pos_y):
        picture = self.get_picture
        for i, line in enumerate(picture):
            stdscr.addstr(pos_y + i, pos_x, line)

    def move(self, x, y):
        self.position = (x, y)

    def click_left(self):
        self.left_button.press()

    def release_all(self):
        self.left_button.release()
        self.right_button.release()
        self.middle_button.release()

    def click_right(self):
        self.right_button.press()

    def click_middle(self):
        self.middle_button.press()
