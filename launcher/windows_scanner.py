import os

from utils.json_manager import save_json

START_MENU_PATHS = [

    os.path.join(
        os.environ["PROGRAMDATA"],
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs"
    ),

    os.path.join(
        os.environ["APPDATA"],
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs"
    )
]

DATABASE_FILE = "database/apps.json"


def scan_windows_apps():

    print("\nScanning Installed Applications...\n")

    apps = []

    seen = set()

    for folder in START_MENU_PATHS:

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith(".lnk"):

                    app_name = os.path.splitext(file)[0]

                    key = app_name.lower()

                    if key in seen:
                        continue

                    seen.add(key)

                    apps.append({

                        "name": app_name,

                        "shortcut": os.path.join(root, file)

                    })

                    print(app_name)

    save_json(DATABASE_FILE, apps)

    print(f"\nSaved {len(apps)} applications to {DATABASE_FILE}")