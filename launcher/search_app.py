from utils.json_manager import load_json
from brain.fuzzy_match import fuzzy_search

DATABASE_FILE = "database/apps.json"


def search_application(user_input):

    apps = load_json(DATABASE_FILE)

    names = [app["name"] for app in apps]

    best_match = fuzzy_search(user_input, names)

    if best_match is None:
        return None

    for app in apps:
        if app["name"] == best_match:
            return app

    return None