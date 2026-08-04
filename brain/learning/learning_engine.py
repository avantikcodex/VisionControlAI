from brain.learning.learner import Learner
from brain.learning.trainer import Trainer
from brain.learning.feedback import FeedbackManager
from brain.learning.experience import ExperienceManager
from brain.learning.knowledge_updater import KnowledgeUpdater
from brain.learning.learning_history import LearningHistory
from brain.learning.self_learning import SelfLearning
from brain.learning.reinforcement import MemoryReinforcement
from brain.learning.continuous_learning import ContinuousLearning
from brain.learning.analytics import LearningAnalytics


class LearningEngine:

    def __init__(self):

        self.learner = Learner()
        self.trainer = Trainer()
        self.feedback = FeedbackManager()
        self.experience = ExperienceManager()
        self.updater = KnowledgeUpdater()
        self.history = LearningHistory()

        # Self Learning
        self.self_learning = SelfLearning()

        # Memory Reinforcement
        self.reinforcement = MemoryReinforcement()

        # Continuous Learning
        self.continuous = ContinuousLearning()

        # Analytics
        self.analytics = LearningAnalytics()

    def learn(self, question, answer):

        # Store experience
        self.experience.store(question, answer)

        # Save history
        self.history.add(question)

        # Learn new knowledge
        self.learner.learn(question, answer)

        # Update knowledge
        self.updater.update(question, answer)

        # Reinforce memory
        self.reinforcement.reinforce(question)

        # Continuous learning cycle
        self.continuous.update()

        # Analytics
        self.analytics.question()

        print(
            f"Memory Score : {self.reinforcement.score(question)}"
        )

        return True

    def feedback_response(self, question, correct):

        # Record feedback
        self.feedback.record(question, correct)

        # Update self-learning statistics
        self.self_learning.update(correct)

        # Analytics
        self.analytics.feedback()

        # Reward or improve
        if correct:
            self.trainer.reward(question)
        else:
            self.trainer.improve(question)

        print(
            f"Learning Accuracy : {self.self_learning.accuracy()}%"
        )