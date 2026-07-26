from knowledge.knowledge_manager import KnowledgeManager

km = KnowledgeManager()

print("=" * 50)
print("KNOWLEDGE MANAGER TEST")
print("=" * 50)

print()

print("Chrome")

print(km.app("google chrome"))

print()

print("YouTube")

print(km.website("youtube"))

print()

print("Intent")

print(km.intent("watch videos"))