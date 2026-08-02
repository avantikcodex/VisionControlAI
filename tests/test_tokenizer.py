from brain.nlu.tokenizer import tokenize

print("=" * 50)
print("TOKENIZER TEST")
print("=" * 50)

while True:

    sentence = input("\nSentence : ")

    if sentence.lower() == "exit":
        break

    print("\nTokens")

    print(tokenize(sentence))