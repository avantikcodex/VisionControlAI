from brain.learning.learning_engine import LearningEngine

engine = LearningEngine()

print("=" * 60)
print("SELF LEARNING TEST")
print("=" * 60)

engine.feedback_response(

    "Python",

    True

)

engine.feedback_response(

    "Java",

    True

)

engine.feedback_response(

    "Physics",

    False

)