from brain.reasoning.context_reasoner import get_context
from brain.reasoning.recommendation import recommend
from brain.reasoning.priority import prioritize


class ReasoningEngine:

    def think(self, sentence):

        context = get_context()

        actions = recommend(sentence)

        actions = prioritize(actions)

        return {

            "context": context,

            "recommendations": actions

        }