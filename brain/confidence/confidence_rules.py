class ConfidenceRules:

    def should_answer(self, score):

        return score >= 70

    def should_search(self, score):

        return 30 <= score < 70

    def should_learn(self, score):

        return score < 30