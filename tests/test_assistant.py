from brain.integration.assistant import Assistant

assistant = Assistant()

print("=" * 60)
print("VEXA ASSISTANT TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    if sentence.lower() == "exit":
        break

    request, reply = assistant.process(sentence)

    print()

    print("Intent :", request.intent)

    print("Entity :", request.entity)

    print("Decision :", request.decision)

    print()

    print("VEXA :", reply)