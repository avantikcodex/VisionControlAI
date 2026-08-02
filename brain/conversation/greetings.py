from random import choice

from brain.conversation.responses import (
    WELCOME_RESPONSES,
    GOOD_MORNING,
    GOOD_AFTERNOON,
    GOOD_EVENING
)


class Greetings:

    def reply(self, sentence):

        sentence = sentence.lower()

        if "good morning" in sentence:
            return choice(GOOD_MORNING)

        if "good afternoon" in sentence:
            return choice(GOOD_AFTERNOON)

        if "good evening" in sentence:
            return choice(GOOD_EVENING)

        if any(word in sentence for word in [
            "hello",
            "hi",
            "hey"
        ]):

            return choice(WELCOME_RESPONSES)

        return None