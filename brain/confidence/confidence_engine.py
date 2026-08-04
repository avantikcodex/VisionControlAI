from brain.confidence.confidence_score import ConfidenceScore
from brain.confidence.confidence_rules import ConfidenceRules


class ConfidenceEngine:

    def __init__(self):

        self.score = ConfidenceScore()
        self.rules = ConfidenceRules()

    def evaluate(self, decision, knowledge_found):

        confidence = self.score.calculate(
            decision,
            knowledge_found
        )

        return {
            "confidence": confidence,
            "answer": self.rules.should_answer(confidence),
            "search": self.rules.should_search(confidence),
            "learn": self.rules.should_learn(confidence)
        }