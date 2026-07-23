import os

def process_command(command):

    print("Received:", command)

    if "open chrome" in command:

        print("Chrome command detected")

        os.system("start https://www.google.com")

    elif "open calculator" in command:

        print("Opening Calculator")

        os.system("calc")

    elif "open notepad" in command:

        print("Opening Notepad")

        os.system("notepad")

    else:

        print("Command not found")