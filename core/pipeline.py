from brain.intent_cleaner import clean_command
from brain.aliases import replace_alias
from brain.ai_router import route
from core.dispatcher import dispatch


def process(command):

    print("\n==============================")
    print("Original :", command)

    # Step 1
    command = clean_command(command)
    print("Cleaned  :", command)

    # Step 2
    command = replace_alias(command)
    print("Alias    :", command)

    # Step 3
    knowledge = route(command)

    if knowledge:

        print("Knowledge :", knowledge)

        command = knowledge["target"]

    # Step 4
    dispatch(command)

    print("==============================")