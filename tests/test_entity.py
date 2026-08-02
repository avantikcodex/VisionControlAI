from brain.nlu.tokenizer import tokenize
from brain.nlu.stopwords import remove_stop_words
from brain.nlu.entity_extractor import extract_entity

print("=" * 50)
print("ENTITY EXTRACTOR TEST")
print("=" * 50)

while True:

    sentence = input("\nSentence : ")

    if sentence.lower() == "exit":
        break

    tokens = tokenize(sentence)

    cleaned = remove_stop_words(tokens)

    entity = extract_entity(cleaned)

    print()

    print("Tokens")

    print(tokens)

    print()

    print("Cleaned")

    print(cleaned)

    print()

    print("Entity")

    print(entity)