from brain.extractor.memory_extractor import process
from brain.memory.memory_engine import MemoryEngine

memory = MemoryEngine()

print("=" * 60)
print("MEMORY EXTRACTOR TEST")
print("=" * 60)

sentences = [
    "My name is Avantik",
    "I study at Ajeenkya DY Patil",
    "I love Python",
    "My favorite IDE is VS Code",
    "My goal is Become AI Engineer"
]

for sentence in sentences:

    process(sentence)

print("\nProfile")
print(memory.profile.load())

print("\nPreferences")
print(memory.preferences.load())

print("\nLong Memory")
print(memory.long_memory.load())