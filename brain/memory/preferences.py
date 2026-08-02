from brain.memory.memory_database import MemoryDatabase

DATABASE = "database/memory/preferences.json"


class Preferences:

    def __init__(self):

        self.database = MemoryDatabase()

    def load(self):

        return self.database.load(DATABASE)

    def save(self, data):

        self.database.save(DATABASE, data)

    def set(self, key, value):

        preferences = self.load()

        preferences[key] = value

        self.save(preferences)

    def get(self, key):

        preferences = self.load()

        return preferences.get(key)