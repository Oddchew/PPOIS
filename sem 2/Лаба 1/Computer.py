import curses
import time
from CPU import CPU
from HardDrive import HardDrive
from Videocard import Videocard  # noqa F401
from Interface import Interface
from Keyboard.Keyboard import Keyboard
from Mouse import Mouse


class Computer:
    def __init__(
            self, freq_cpu, freq_ram, capac_ram, capac_harddrive, type_hd
    ):
        self.cpu = CPU(freq_cpu)  # noqa F401
        self.hardDrive = HardDrive(capac_harddrive, type_hd)  # noqa F401
        self.videocard = Videocard()
        self.keyboard = Keyboard()
        self.mouse = Mouse()
        self.key_map = {
            curses.KEY_UP: 'Up',
            curses.KEY_DOWN: 'Down',
            curses.KEY_LEFT: 'Left',
            curses.KEY_RIGHT: 'Right',
            curses.KEY_BACKSPACE: 'Backspace',
            curses.KEY_ENTER: 'Enter'
        }

    def install_os(self, OS):
        self.hardDrive.OS = {"OS": OS, "Version": 1.0}
        self.hardDrive.save()

    def turn(self, monitor):
        monitor.frame = self.videocard.turn(monitor.resolution, 24,
                                            self.hardDrive.OS["OS"])

    def mouse_capture(self, stdscr, monitor):
        interface = Interface(1, 8)
        interface.change_n(-1)
        while (True):
            key = stdscr.getch()
            if key == ord('q') - 96 or key == 27:
                break
            elif key in self.key_map:
                label = self.key_map[key]
                self.keyboard.press_key(label)
            else:
                label = chr(key)
                self.keyboard.press_key(label)
            if self.keyboard.status:
                self.keyboard.display(stdscr)

            fields = [
                      "Установить приложение", "Обновить ОС"]
            interface.display(stdscr, fields)
            stdscr.addstr(7, 0, self.monitor.get_monitor_text)
            if key == curses.KEY_UP:
                interface.update('Up')

            if key == curses.KEY_DOWN:
                interface.update('Down')

            if key == 10:  # Enter
                i = interface.choosed_field()
                if i == -1:
                    return
                choosen_field = fields[i]  # Запоминаем выбранное поле
                if choosen_field == "Обновить ОС":
                    str = self.cpu.update_OS(self.hardDrive)
                    for j in range(str.__len__()):
                        stdscr.addstr(10, 1 + j, str[i])
                        stdscr.refresh()
                        time.sleep(1)
                if choosen_field == "Установить приложение":
                    self.cpu.install_app(stdscr)

            stdscr.addstr(7, 0, monitor.get_monitor_text)
            interface.display(stdscr, fields)
            if self.keyboard.status:
                self.keyboard.display(stdscr)
            stdscr.refresh()
            time.sleep(0.1)
