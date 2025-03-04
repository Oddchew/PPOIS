class Key:
    def __init__(self, label):
        self.label = label
        self.pressed = False

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False

    def get_display_label(self):
        return f"[{self.label}]"

    def __str__(self):
        return self.label
