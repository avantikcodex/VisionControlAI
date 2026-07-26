from core.pipeline import process

print("=" * 50)
print("VISIONCONTROL AI PIPELINE TEST")
print("=" * 50)

while True:

    command = input("\nYou : ")

    if command.lower() == "exit":
        break

    process(command)