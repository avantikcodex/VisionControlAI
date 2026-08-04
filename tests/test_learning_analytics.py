from brain.learning.learning_engine import LearningEngine

engine = LearningEngine()

print("=" * 60)
print("LEARNING ANALYTICS TEST")
print("=" * 60)

engine.learn("Python", "Programming")

engine.learn("Java", "Programming")

engine.feedback_response("Python", True)

engine.feedback_response("Java", False)

print()

print(engine.analytics.report())