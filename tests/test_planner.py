from brain.planning.planner import Planner

planner = Planner()

print("=" * 60)
print("PLANNING ENGINE TEST")
print("=" * 60)

while True:

    sentence = input("\nYou : ")

    if sentence.lower() == "exit":
        break

    plan = planner.create_plan(sentence)

    print("\nPlan")

    for i, task in enumerate(plan.all(), start=1):

        print(f"{i}. {task}")