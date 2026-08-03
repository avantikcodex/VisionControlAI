from brain.core.vexa_core import VexaCore
from brain.integration.response_handler import ResponseHandler


class Assistant:

    def __init__(self):

        self.core = VexaCore()
        self.response = ResponseHandler()

    def process(self, sentence):

        request = self.core.execute(sentence)

        reply = self.response.build(request)

        return request, reply