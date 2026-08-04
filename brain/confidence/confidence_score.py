class ConfidenceScore:

    def calculate(self, decision, knowledge_found):

        if decision is None:
            return 0

        if knowledge_found:
            return 95

        return 40