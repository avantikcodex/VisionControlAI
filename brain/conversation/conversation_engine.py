from brain.conversation.greetings import Greetings
from brain.conversation.smalltalk import SmallTalk
from brain.conversation.conversation_state import ConversationState


class ConversationEngine:

    def __init__(self):

        self.greetings = Greetings()

        self.smalltalk = SmallTalk()

        self.state = ConversationState()

    def reply(self, sentence):

        response = self.greetings.reply(sentence)

        if response:

            self.state.remember("Greeting", response)

            return response

        response = self.smalltalk.reply(sentence)

        if response:

            self.state.remember("SmallTalk", response)

            return response

        return None