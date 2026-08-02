from rapidfuzz import fuzz
from utils.json_manager import load_json

DATABASE = "database/apps.json"


def get_all_apps():
    return load_json(DATABASE)


def find_app(name):

    apps = get_all_apps()

    name = name.lower().strip()

    best_match = None
    highest_score = 0

    for app in apps:

        app_name = app["name"].lower()

        # Exact match
        if name == app_name:
            return app

        # Partial match
        if name in app_name:
            return app

        # Fuzzy match
        score = fuzz.ratio(name, app_name)

        if score > highest_score:
            highest_score = score
            best_match = app

    if highest_score >= 65:
        return best_match

    return None