import os
import webbrowser


def open_application(app_name):

    app_name = app_name.lower()

    if app_name == "chrome":

        print("Opening Chrome...")

        webbrowser.open("https://www.google.com")

    elif app_name == "calculator":

        print("Opening Calculator...")

        os.system("calc")

    elif app_name == "notepad":

        print("Opening Notepad...")

        os.system("notepad")

    elif app_name == "settings":

        print("Opening Settings...")

        os.system("start ms-settings:")