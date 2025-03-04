import json


class HardDrive(object):
    def __init__(self, capacity, type_):
        self.type = type_
        self.files = {}
        self.capacity = capacity
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                self.OS = json.load(file)
            if not isinstance(self.OS, dict):
                self.OS = {
                    "OS": "None",
                    "Version": 1.0
                    }
        except (FileNotFoundError, json.JSONDecodeError):
            self.OS = {
                "OS": "None",
                "Version": 1.0
                }

    def save(self):
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(self.OS, file, ensure_ascii=False, indent=4)
