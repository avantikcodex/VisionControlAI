from brain.planning.plan import Plan
from brain.planning.task import Task


class Planner:

    def create_plan(self, sentence):

        sentence = sentence.lower()

        plan = Plan()

        if "exam" in sentence:

            plan.add(Task("Open Notes"))
            plan.add(Task("Revise Chapters"))
            plan.add(Task("Solve Previous Year Questions"))
            plan.add(Task("Take Short Break"))
            plan.add(Task("Final Revision"))

        elif "project" in sentence:

            plan.add(Task("Open VS Code"))
            plan.add(Task("Open Project Folder"))
            plan.add(Task("Continue Last Module"))
            plan.add(Task("Save Progress"))

        elif "study" in sentence:

            plan.add(Task("Open Study Material"))
            plan.add(Task("Start Focus Timer"))
            plan.add(Task("Practice Questions"))

        return plan