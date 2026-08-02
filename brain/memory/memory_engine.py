from brain.memory.user_profile import UserProfile
from brain.memory.preferences import Preferences
from brain.memory.long_memory import LongMemory
from brain.memory.short_memory import ShortMemory
from brain.memory.session import Session


class MemoryEngine:

    def __init__(self):

        self.profile = UserProfile()

        self.preferences = Preferences()

        self.long_memory = LongMemory()

        self.short_memory = ShortMemory()

        self.session = Session()