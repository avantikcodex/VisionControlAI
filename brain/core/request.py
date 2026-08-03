class Request:

    def __init__(self, sentence):

        self.original = sentence
        self.intent = None
        self.entity = None
        self.decision = None