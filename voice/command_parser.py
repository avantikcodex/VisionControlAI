from commands.command_engine import execute_command


def process_command(command):

    success = execute_command(command)

    if not success:

        print("Sorry, I don't know that command yet.")