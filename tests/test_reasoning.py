from brain.reasoning.reasoning_engine import ReasoningEngine

engine = ReasoningEngine()

print("=" * 60)
print("REASONING ENGINE TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    if sentence.lower() == "exit":
        break

    result = engine.think(sentence)

    print("\nContext")

    print(result["context"])

    print("\nRecommendations")

    if result["recommendations"]:

        for recommendation in result["recommendations"]:

            print("-", recommendation)

    else:

        print("No recommendation.")