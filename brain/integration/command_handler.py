from brain.core.request import Request


class CommandHandler:

    def create_request(self, sentence):

        return Request(sentence)