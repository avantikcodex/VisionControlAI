from commands.command_database import COMMANDS


def detect_intent(command):

    command = command.lower().strip()

    best_match = None

    highest_score = 0

    for intent, phrases in COMMANDS.items():

        score = 0

        for phrase in phrases:

            words = phrase.split()

            for word in words:

                if word in command:

                    score += 1

        if score > highest_score:

            highest_score = score

            best_match = intent

    return best_match