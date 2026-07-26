from core.dispatcher import dispatch

print("===== Browser Skill Test =====")

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        break

    dispatch(command)