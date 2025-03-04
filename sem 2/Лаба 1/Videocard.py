class Videocard:
    def turn(self, width, height, os):
        lines = [' ' * (width - 2) for _ in range(height - 2)]
        middle = height // 2  # Центр по высоте
        с = (width - 2) // 2  # Центр по ширине

        if os == "Windows":
            # Логотип Windows (окно из 4-х частей)
            lines[middle - 1] = ' ' * (с - 2) + "█ █" + ' ' * (с - 1)
            lines[middle + 1] = ' ' * (с - 2) + "█ █" + ' ' * (с - 1)

        elif os == "Linux":
            # Логотип Linux (пингвин)
            lines[middle - 3] = ' ' * (с - 1) + '███' + ' ' * (с - 2)
            lines[middle - 2] = ' ' * (с - 2) + '█ █ █' + ' ' * (с - 3)
            lines[middle - 1] = ' ' * (с - 2) + '█████' + ' ' * (с - 3)
            lines[middle] = ' ' * (с - 3) + '███ ███' + ' ' * (с - 4)
            lines[middle + 1] = ' ' * (с - 2) + '█████' + ' ' * (с - 3)
            lines[middle + 2] = ' ' * (с - 2) + '██ ██' + ' ' * (с - 3)
            lines[middle + 3] = ' ' * (с - 1) + '█ █' + ' ' * (с - 2)
        else:
            len = os.__len__()//2
            lines[middle] = ' ' * (с - len) + os + ' ' * (с - len)

        return lines
