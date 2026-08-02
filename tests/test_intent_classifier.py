from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words
from brain.nlu.intent_classifier import classify_intent

print("="*50)
print("INTENT CLASSIFIER TEST")
print("="*50)

while True:

    sentence = input("\nSentence : ")

    if sentence.lower() == "exit":
        break

    tokens = tokenize(sentence)

    cleaned = remove_stop_words(tokens)

    print("\nTokens")

    print(tokens)

    print("\nCleaned")

    print(cleaned)

    print("\nIntent")

    print(classify_intent(cleaned))