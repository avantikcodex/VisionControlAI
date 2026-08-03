from brain.memory.memory_engine import MemoryEngine

memory = MemoryEngine()


def get_context():

    return {

        "profile": memory.profile.load(),

        "preferences": memory.preferences.load(),

        "goals": memory.long_memory.load()

    }