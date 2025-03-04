import json # noqa F401
import time
import curses
from Computer import Computer
from Monitor import Monitor
from Interface import Interface

KEY_ENTER = 10
KEY_ESC = 27
KEY_CTRL_Q = ord('q') - 96


def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.clear()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # On
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Keys

    stdscr.addstr(0, 0, " _______")
    stdscr.addstr(1, 0, "|       |")

    stdscr.addstr(2, 0, "|  ")
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 3, "ON")
    stdscr.attroff(curses.color_pair(1))

    stdscr.addstr(2, 5, "   |")
    stdscr.addstr(3, 0, "|_______|")

    stdscr.refresh()

    status = False

    while True:
        key = stdscr.getch()
        if key == KEY_ENTER:
            computer = Computer(3500, 4200, 16, 1000, "SSD")
            status = True
            break
        if key == KEY_ESC:
            break

    if status:
        fields = [
            "Подключить монитор", "Подключить клавиатуру", "Подключить мышь"
        ]
        mainI = Interface()
        monitor = Monitor(100, 60)
        statusMonitor = False

        stdscr.clear()
        mainI.display(stdscr, fields)
        time.sleep(0.1)

        while status:
            key = stdscr.getch()
            computer.keyboard.release_all()

            if key == KEY_CTRL_Q and monitor.get_monitor_status():
                computer.mouse_capture(stdscr, monitor)
            elif key in computer.key_map:
                label = computer.key_map[key]
                computer.keyboard.press_key(label)
            else:
                label = chr(key)
                computer.keyboard.press_key(label)

            if key == curses.KEY_UP:
                mainI.update('Up')

            if key == curses.KEY_DOWN:
                mainI.update('Down')

            if key == KEY_ENTER:
                i = mainI.choosed_field()
                if i == -1:
                    stdscr.clear()
                    stdscr.refresh()
                    break
                choosen_field = fields[i]
                fields.remove(choosen_field)
                mainI.change_n(-1)
                if choosen_field == "Подключить клавиатуру":
                    computer.keyboard.status = True

                if choosen_field == "Подключить монитор":
                    statusMonitor = True
                    mainI.change_n(1)
                    fields.append("Включить монитор")

                if choosen_field == "Подключить мышь":
                    computer.mouse.status = True

                if choosen_field == "Включить монитор":
                    if computer.hardDrive.OS["OS"] == "None":
                        stdscr.clear()
                        stdscr.addstr(0, 0, "Выберите устанавливаемую ОС")
                        stdscr.refresh()
                        time.sleep(3)
                        OsInterface = Interface()
                        OsInterface.change_n(-1)
                        OsFilds = ["Linux", "Windows"]
                        OsInterface.display(stdscr, OsFilds)
                        stdscr.refresh()
                        while computer.hardDrive.OS["OS"] == "None":
                            key = stdscr.getch()
                            if key == curses.KEY_UP:
                                OsInterface.update('Up')

                            if key == curses.KEY_DOWN:
                                OsInterface.update('Down')

                            if key == KEY_ENTER:
                                i = OsInterface.choosed_field()
                                choose = OsFilds[i]
                                if i == -1:
                                    return
                                elif choose == "Linux":
                                    computer.install_os("Linux")
                                elif choose == "Windows":
                                    computer.install_os("Windows")
                            stdscr.clear()
                            OsInterface.display(stdscr, OsFilds)
                            stdscr.refresh()

                    computer.turn(monitor)
                    monitor.enable_monitor()
                    stdscr.refresh()

            if key == KEY_ESC:
                status = False

            stdscr.clear()
            mainI.display(stdscr, fields)
            if statusMonitor:
                stdscr.addstr(7, 0, monitor.get_monitor_text)
            if computer.keyboard.status:
                computer.keyboard.display(stdscr)
            if computer.mouse.status:
                computer.mouse.draw_mouse(stdscr, 120, 7)
                if statusMonitor:
                    x = computer.mouse.position[0]
                    y = computer.mouse.position[1]
                    if key == curses.KEY_MOUSE:
                        stdscr.addstr(8 + y, 1 + x, ' ')
                        _, x, y, _, button = curses.getmouse()
                        x -= 1
                        y -= 8
                        if x > monitor.resolution - 3:
                            x = monitor.resolution - 3
                        if x < 0:
                            x = 0
                        if y > 24 - 3:
                            y = 24 - 3
                        if y < 0:
                            y = 0
                        computer.mouse.move(x, y)  # Обновляем позицию

                        if button & curses.BUTTON1_PRESSED:
                            computer.mouse.click_left()
                        elif button & curses.BUTTON3_PRESSED:
                            computer.mouse.click_right()
                        elif button & curses.BUTTON2_PRESSED:
                            computer.mouse.click_middle()
                        elif button & curses.BUTTON1_RELEASED:
                            computer.mouse.release_all()

                    stdscr.addstr(8 + y, 1 + x, '*')
            stdscr.refresh()

            time.sleep(0.1)

    stdscr.addstr(0, 0, "OK")
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
