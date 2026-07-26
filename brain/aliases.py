ALIASES = {

    "vs code": "visual studio code",

    "vscode": "visual studio code",

    "youtube videos": "youtube",

    "google search": "google"

}


def replace_alias(command):

    command = command.lower()

    for alias, value in ALIASES.items():

        command = command.replace(alias, value)

    return command