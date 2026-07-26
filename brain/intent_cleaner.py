REMOVE_WORDS = [
    "open",
    "launch",
    "start",
    "run",
    "please",
    "can",
    "you",
    "vexa",
    "hey",
    "for",
    "me",
    "the",
]


def clean_command(command):

    command = command.lower()

    words = command.split()

    cleaned = []

    for word in words:

        if word not in REMOVE_WORDS:

            cleaned.append(word)

    return " ".join(cleaned)