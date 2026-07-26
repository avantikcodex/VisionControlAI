from commands.intent_engine import detect_intent
from launcher.app_launcher import launch_app


def execute_command(command):

    intent = detect_intent(command)

    if intent is None:
        return False

    app_map = {

        "open_chrome": "chrome",

        "open_notepad": "notepad",

        "open_calculator": "calculator",

        "open_settings": "settings",

        "open_paint": "paint",

        "open_cmd": "cmd",

        "open_powershell": "powershell"

    }

    if intent in app_map:

        launch_app(app_map[intent])

        return True

    return False