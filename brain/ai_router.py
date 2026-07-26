from utils.json_manager import load_json

DATABASE = "database/intents.json"


def route(command):

    command = command.lower()

    intents = load_json(DATABASE)

    for item in intents:

        if item["intent"] in command:

            return item

    return None