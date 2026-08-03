from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words
from brain.nlu.intent_classifier import classify_intent
from brain.nlu.entity_extractor import extract_entity

from brain.decision.decision_engine import DecisionEngine


class Pipeline:

    def process(self, request):

        # Step 1
        tokens = tokenize(request.original)

        # Step 2
        tokens = remove_stop_words(tokens)

        # Step 3
        request.intent = classify_intent(tokens)

        # Step 4
        request.entity = extract_entity(tokens)

        # Step 5
        engine = DecisionEngine()

        request.decision = engine.make_decision(
            request.intent,
            request.entity
        )

        return request