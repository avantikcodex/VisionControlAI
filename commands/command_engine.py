from commands.command_database import COMMANDS
from commands.app_commands import open_application


def execute_command(command):

    command = command.lower().strip()

    for action, phrases in COMMANDS.items():

        for phrase in phrases:

            if phrase in command:

                if action == "open_chrome":
                    open_application("chrome")

                elif action == "open_calculator":
                    open_application("calculator")

                elif action == "open_notepad":
                    open_application("notepad")

                elif action == "open_settings":
                    open_application("settings")

                return True

    return False