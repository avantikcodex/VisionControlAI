class LearningAnalytics:

    def __init__(self):

        self.total_questions = 0
        self.total_feedback = 0

    def question(self):

        self.total_questions += 1

    def feedback(self):

        self.total_feedback += 1

    def report(self):

        return {

            "Questions Learned": self.total_questions,

            "Feedback Received": self.total_feedback

        }