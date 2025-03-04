from RAM import RAM
textInstall = "Для установки нажмите д, для отмены нажмите н"


class CPU:
    def __init__(self, freq):
        self.freq = freq

    def install_app(self, stdscr):
        app = RAM.get_random_application()
        stdscr.addstr(11, 1, app["name"])
        stdscr.refresh()
        stdscr.addstr(10, 1, textInstall)
        key = stdscr.getch()
        while (key != ord('д') and key != ord('н') and key != 27):
            key = stdscr.getch()
        if key == ord('д'):
            RAM.save_applications_to_file(app)

    def update_OS(self, hardDrive):
        hardDrive.OS["Version"] += 0.1
        hardDrive.save()
        return '██████████'
