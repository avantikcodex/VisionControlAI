from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words

print("=" * 50)
print("STOP WORD TEST")
print("=" * 50)

while True:

    sentence = input("\nSentence : ")

    if sentence.lower() == "exit":
        break

    tokens = tokenize(sentence)

    print("\nTokens")

    print(tokens)

    print("\nAfter Removing Stop Words")

    print(remove_stop_words(tokens))