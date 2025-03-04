import curses
from colorama import init
from Keyboard.Key import Key

init(autoreset=True)


class Keyboard:
    def __init__(self):
        self.keys = [
            [Key('Esc'), Key('F1'), Key('F2'), Key('F3'), Key('F4'),
             Key('F5'), Key('F6'), Key('F7'), Key('F8'), Key('F9'),
             Key('F10'), Key('F11'), Key('F12')],

            [Key('`'), Key('1'), Key('2'), Key('3'), Key('4'),
             Key('5'), Key('6'), Key('7'), Key('8'), Key('9'),
             Key('0'), Key('-'), Key('='), Key('Backspace')],

            [Key('Tab'), Key('q'), Key('w'), Key('e'), Key('r'),
             Key('t'), Key('y'), Key('u'), Key('i'), Key('o'),
             Key('p'), Key('['), Key(']'), Key('\\')],

            [Key('CapsLock'), Key('a'), Key('s'), Key('d'), Key('f'),
             Key('g'), Key('h'), Key('j'), Key('k'), Key('l'),
             Key(';'), Key("'"), Key('Enter')],

            [Key('Shift'), Key('z'), Key('x'), Key('c'), Key('v'),
             Key('b'), Key('n'), Key('m'), Key(','), Key('.'),
             Key('/'), Key('Shift')],

            [Key('Ctrl'), Key('Win'), Key('Alt'), Key('Space'), Key('Alt'),
             Key('Ctrl')],

            [Key('Up'), Key('Left'), Key('Down'), Key('Right')]
        ]
        self.buttons = []
        self.status = False

    def press_key(self, key_label):
        for row in self.keys:
            for key in row:
                if key.label == key_label:
                    key.press()
                    print(f"Клавиша {key_label} нажата.")
                    return
        print(f"Клавиша {key_label} не найдена.")

    def release_key(self, key_label):
        for row in self.keys:
            for key in row:
                if key.label == key_label:
                    key.release()
                    print(f"Клавиша {key_label} отпущена.")
                    return
        print(f"Клавиша {key_label} не найдена.")

    def display(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()  # Получаем размер экрана
        for i, row in enumerate(self.keys):
            if i + 31 >= max_y:
                break
            for j, key in enumerate(row):
                x = j * 10
                if x + 9 > max_x:
                    continue
                label = key.get_display_label().center(9)
                if key.pressed:
                    stdscr.addstr(i + 31, x, label, curses.color_pair(2))
                else:
                    stdscr.addstr(i + 31, x, label)

    def release_all(self):
        for row in self.keys:
            for key in row:
                key.release()
