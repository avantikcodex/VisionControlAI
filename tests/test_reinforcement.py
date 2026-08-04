from brain.learning.learning_engine import LearningEngine

engine = LearningEngine()

print("=" * 60)
print("MEMORY REINFORCEMENT TEST")
print("=" * 60)

engine.learn(

    "Open Chrome",

    "Chrome"

)

engine.learn(

    "Open Chrome",

    "Chrome"

)

engine.learn(

    "Open Chrome",

    "Chrome"

)

engine.learn(

    "Open VS Code",

    "VS Code"

)

print()

print(engine.reinforcement.all())

print()

print(

    "Strongest Memory :",

    engine.reinforcement.strongest()

)