from brain.reasoning.rules import RULES


def recommend(sentence):

    sentence = sentence.lower()

    for keyword, actions in RULES.items():

        if keyword in sentence:

            return actions

    return []