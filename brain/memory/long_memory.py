from brain.memory.memory_database import MemoryDatabase

DATABASE = "database/memory/long_memory.json"


class LongMemory:

    def __init__(self):

        self.database = MemoryDatabase()

    def load(self):

        return self.database.load(DATABASE)

    def save(self, memory):

        self.database.save(DATABASE, memory)

    def remember(self, key, value):

        memory = self.load()

        memory[key] = value

        self.save(memory)

    def recall(self, key):

        memory = self.load()

        return memory.get(key)