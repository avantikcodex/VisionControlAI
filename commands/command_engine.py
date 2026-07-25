from commands.intent_engine import detect_intent
from commands.app_commands import open_application


def execute_command(command):

    intent = detect_intent(command)

    if intent is None:
        return False

    if intent == "open_chrome":
        open_application("chrome")

    elif intent == "open_calculator":
        open_application("calculator")

    elif intent == "open_notepad":
        open_application("notepad")

    elif intent == "open_settings":
        open_application("settings")

    else:
        return False

    return True