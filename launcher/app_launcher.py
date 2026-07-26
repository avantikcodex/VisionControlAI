import os


def launch_application(app):

    if app is None:

        print("Application not found.")

        return False

    shortcut = app["shortcut"]

    print("Launching:", app["name"])

    os.startfile(shortcut)

    return True