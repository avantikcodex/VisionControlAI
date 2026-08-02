from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words
from brain.nlu.intent_classifier import classify_intent
from brain.nlu.entity_extractor import extract_entity

from brain.decision.decision_engine import DecisionEngine
from brain.decision.dispatcher import Dispatcher

engine = DecisionEngine()
dispatcher = Dispatcher()

print("=" * 60)
print("VISIONCONTROL AI - COMPLETE PIPELINE")
print("=" * 60)

while True:

    command = input("\nYou : ")

    if command.lower() == "exit":
        break

    tokens = tokenize(command)

    cleaned = remove_stop_words(tokens)

    intent = classify_intent(cleaned)

    entity = extract_entity(cleaned)

    decision = engine.make_decision(intent, entity)

    print("\nIntent :", intent)
    print("Entity :", entity)
    print("Decision :", decision)

    dispatcher.dispatch(decision)