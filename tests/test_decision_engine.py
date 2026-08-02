from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words
from brain.nlu.intent_classifier import classify_intent
from brain.nlu.entity_extractor import extract_entity

from brain.decision.decision_engine import DecisionEngine

engine = DecisionEngine()

print("=" * 60)
print("DECISION ENGINE TEST")
print("=" * 60)

while True:

    sentence = input("\nSentence : ")

    if sentence.lower() == "exit":
        break

    tokens = tokenize(sentence)

    cleaned = remove_stop_words(tokens)

    intent = classify_intent(cleaned)

    entity = extract_entity(cleaned)

    decision = engine.make_decision(intent, entity)

    print("\nIntent")
    print(intent)

    print("\nEntity")
    print(entity)

    print("\nDecision")
    print(decision)