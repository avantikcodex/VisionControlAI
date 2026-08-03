from brain.core.vexa_core import VexaCore

core = VexaCore()

print("=" * 60)
print("VEXA CORE TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    if sentence.lower() == "exit":
        break

    request = core.execute(sentence)

    print()

    print("Intent")
    print(request.intent)

    print()

    print("Entity")
    print(request.entity)

    print()

    print("Decision")
    print(request.decision)