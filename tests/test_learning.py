from brain.learning.learning_engine import LearningEngine

engine = LearningEngine()

print("=" * 60)
print("LEARNING ENGINE TEST")
print("=" * 60)

engine.learn(

    "What is Python?",

    "Python is a programming language."

)

engine.feedback_response(

    "What is Python?",

    True

)