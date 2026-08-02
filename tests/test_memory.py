from brain.memory.memory_engine import MemoryEngine

memory = MemoryEngine()

print("=" * 50)
print("MEMORY ENGINE TEST")
print("=" * 50)

memory.profile.set("name", "Avantik")
memory.profile.set("college", "Ajeenkya DY Patil")

memory.preferences.set("browser", "Chrome")
memory.preferences.set("ide", "VS Code")

memory.long_memory.remember(
    "goal",
    "Become AI Engineer"
)

memory.short_memory.remember(
    "current_task",
    "Building VisionControl AI"
)

print()

print("Profile")
print(memory.profile.load())

print()

print("Preferences")
print(memory.preferences.load())

print()

print("Long Memory")
print(memory.long_memory.load())

print()

print("Short Memory")
print(memory.short_memory.memory)