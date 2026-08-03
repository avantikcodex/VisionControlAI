from brain.knowledge.knowledge_engine import KnowledgeEngine

engine = KnowledgeEngine()

print("=" * 60)
print("KNOWLEDGE ENGINE TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    data = engine.process(sentence)

    print("\nQuery :", data["query"])
    print("Topic :", data["topic"])
    print("Destination :", data["destination"])
    print("Source :", data["result"]["source"])

    print("\nVEXA\n")
    print(data["answer"])