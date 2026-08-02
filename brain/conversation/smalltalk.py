from random import choice

from brain.conversation.responses import (
    HOW_ARE_YOU,
    THANK_YOU,
    WHO_ARE_YOU
)


class SmallTalk:

    def reply(self, sentence):

        sentence = sentence.lower()

        if "how are you" in sentence:
            return choice(HOW_ARE_YOU)

        if "thank" in sentence:
            return choice(THANK_YOU)

        if "who are you" in sentence:
            return choice(WHO_ARE_YOU)

        return None