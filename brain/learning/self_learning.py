class SelfLearning:

    def __init__(self):

        self.correct = 0
        self.wrong = 0

    def update(self, feedback):

        if feedback:

            self.correct += 1

        else:

            self.wrong += 1

    def accuracy(self):

        total = self.correct + self.wrong

        if total == 0:
            return 0

        return round((self.correct / total) * 100, 2)