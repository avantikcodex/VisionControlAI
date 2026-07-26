BROWSER_WORDS = [

    "youtube",

    "google",

    "amazon",

    "github",

    "gmail",

    "chatgpt",

    "netflix",

    "spotify",

    "linkedin",

    "stackoverflow"

]


def classify(command):

    command = command.lower()

    for word in BROWSER_WORDS:

        if word in command:

            return "BROWSER"

    return "APPLICATION"