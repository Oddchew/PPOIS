class Monitor:
    def __init__(self, resolution, refresh_rate):
        self.resolution = resolution
        self.refresh_rate = refresh_rate
        self.status = False
        self.frame = [' ' * (resolution - 2)] * 22

    @property
    def get_monitor_text(self):
        width = self.resolution
        height = 24
        lines = ['#' + ' ' * (width - 2) + '#' for _ in range(height)]

        if self.status:
            filled_char = '#'
            middle_start = height // 3
            middle_end = 2 * height // 3
            for i in range(middle_start, middle_end):
                lines[i] = '#' + filled_char * (width - 2) + '#'

        for i in range(height - 2):
            lines[i + 1] = '#' + self.frame[i] + '#'

        lines[0] = '#' * width
        if self.status:
            lines[-2] = '#' + ' ' * (width - 3) + 2 * '*'
            lines[-1] = '#' * (width - 2) + 2 * '*'
        else:
            lines[-2] = '#' + ' ' * (width - 3) + 2 * '.'
            lines[-1] = '#' * (width - 2) + 2 * '.'

        return '\n'.join(lines)

    def enable_monitor(self):
        self.status = True

    def disable_monitor(self):
        self.status = False

    def get_monitor_resolution(self):
        return self.__resolution
