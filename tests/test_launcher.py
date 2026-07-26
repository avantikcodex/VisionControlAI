from brain.intent_cleaner import clean_command
from launcher.search_app import search_application
from launcher.app_launcher import launch_application

print("=" * 50)
print("VEXA LAUNCHER TEST")
print("=" * 50)

while True:

    command = input("\nYou: ").strip()

    if command.lower() == "exit":
        print("Goodbye!")
        break

    cleaned = clean_command(command)

    print("Cleaned :", cleaned)

    app = search_application(cleaned)

    if app is None:
        print("Application not found.")
        continue

    print("Matched :", app["name"])

    launch_application(app)