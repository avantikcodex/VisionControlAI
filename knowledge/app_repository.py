from utils.json_manager import load_json

DATABASE = "database/apps.json"


def get_all_apps():
    return load_json(DATABASE)


def find_app(name):

    apps = get_all_apps()

    name = name.lower()

    for app in apps:

        if name == app["name"].lower():

            return app

    return None