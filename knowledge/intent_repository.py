from utils.json_manager import load_json

DATABASE = "database/intents.json"


def get_all_intents():

    return load_json(DATABASE)


def find_intent(command):

    intents = get_all_intents()

    command = command.lower()

    for item in intents:

        if item["intent"] in command:

            return item

    return None