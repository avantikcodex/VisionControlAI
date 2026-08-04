from brain.learning.learning_engine import LearningEngine

engine = LearningEngine()

print("=" * 60)
print("CONTINUOUS LEARNING TEST")
print("=" * 60)

engine.learn(

    "Python",

    "Programming Language"

)

engine.learn(

    "Java",

    "Programming Language"

)

engine.learn(

    "Physics",

    "Science"

)

print()

print(

    "Total Learning Cycles :",

    engine.continuous.total_cycles()

)