from brain.core.pipeline import Pipeline
from brain.core.request import Request

from brain.decision.dispatcher import Dispatcher


class VexaCore:

    def __init__(self):

        self.pipeline = Pipeline()
        self.dispatcher = Dispatcher()

    def execute(self, sentence):

        request = Request(sentence)

        request = self.pipeline.process(request)

        self.dispatcher.dispatch(request.decision)

        return request