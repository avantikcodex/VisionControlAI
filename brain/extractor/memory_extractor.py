from brain.extractor.profile_extractor import extract_profile
from brain.extractor.preference_extractor import extract_preferences
from brain.extractor.goal_extractor import extract_goal

from brain.memory.memory_engine import MemoryEngine


memory = MemoryEngine()


def process(sentence):

    profile = extract_profile(sentence)

    for key, value in profile.items():

        memory.profile.set(key, value)

    preferences = extract_preferences(sentence)

    for key, value in preferences.items():

        memory.preferences.set(key, value)

    goals = extract_goal(sentence)

    for key, value in goals.items():

        memory.long_memory.remember(key, value)