from skills.application_skill import ApplicationSkill
from skills.browser_skill import BrowserSkill


class SkillManager:

    def __init__(self):

        self.skills = [

            BrowserSkill(),

            ApplicationSkill()

        ]

    def execute(self, intent, command):

        for skill in self.skills:

            if skill.name == intent:

                return skill.execute(command)

        return False