from brain.memory.memory_database import MemoryDatabase

DATABASE = "database/memory/session.json"


class Session:

    def __init__(self):

        self.database = MemoryDatabase()

    def load(self):

        return self.database.load(DATABASE)

    def save(self, data):

        self.database.save(DATABASE, data)