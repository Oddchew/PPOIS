import json
import random

MaxIter = 100
applications = [
    {"name": "Google Chrome", "category": "Browser",
     "size": "200MB", "rating": 4.7},
    {"name": "Visual Studio Code", "category": "IDE",
     "size": "150MB", "rating": 4.8},
    {"name": "Spotify", "category": "Music",
     "size": "500MB", "rating": 4.5},
    {"name": "Slack", "category": "Communication",
     "size": "250MB", "rating": 4.4},
    {"name": "Zoom", "category": "Video Conferencing",
     "size": "300MB", "rating": 4.6},
    {"name": "VLC Media Player", "category": "Media",
     "size": "150MB", "rating": 4.9},
    {"name": "Notepad++", "category": "Text Editor",
     "size": "10MB", "rating": 4.7},
    {"name": "Minecraft", "category": "Game",
     "size": "1.5GB", "rating": 4.8},
    {"name": "Adobe Photoshop", "category": "Design",
     "size": "2GB", "rating": 4.5},
    {"name": "Microsoft Office", "category": "Productivity",
     "size": "5GB", "rating": 4.3}
            ]


class RAM:
    @staticmethod
    def get_random_application(filename="application.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                used_apps = json.load(file)
            if not isinstance(used_apps, dict):
                used_apps = {}
        except (FileNotFoundError, json.JSONDecodeError):
            used_apps = {}

        used_app_names = set(used_apps.keys())

        available_apps = [app for app in applications
                          if app["name"] not in used_app_names]

        if available_apps:
            return random.choice(available_apps)
        else:
            return {"name": "None"}

    @staticmethod
    def save_applications_to_file(random_apps, filename="application.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                existing_apps = json.load(file)
            if not isinstance(existing_apps, dict):
                existing_apps = {}
        except (FileNotFoundError, json.JSONDecodeError):
            existing_apps = {}

        if not isinstance(random_apps, list):
            random_apps = [random_apps]

        for app in random_apps:
            app_name = app.get("name")
            if app_name and app_name != "None":
                existing_apps[app_name] = app

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_apps, file, ensure_ascii=False, indent=4)
