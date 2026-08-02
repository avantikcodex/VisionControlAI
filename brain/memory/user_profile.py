from brain.memory.memory_database import MemoryDatabase

PROFILE = "database/memory/profile.json"


class UserProfile:

    def __init__(self):

        self.database = MemoryDatabase()

    def load(self):

        return self.database.load(PROFILE)

    def save(self, profile):

        self.database.save(PROFILE, profile)

    def set(self, key, value):

        profile = self.load()

        profile[key] = value

        self.save(profile)

    def get(self, key):

        profile = self.load()

        return profile.get(key)