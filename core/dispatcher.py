from core.intent_classifier import classify
from core.skill_manager import SkillManager

manager = SkillManager()


def dispatch(command):

    intent = classify(command)

    return manager.execute(intent, command)