class LearningHistory:

    def __init__(self):

        self.history = []

    def add(self, question):

        self.history.append(question)

        print("[History] Added")