import time

from voice.wake_word import wait_for_vexa
from voice.speech_recognition import listen_command
from voice.command_parser import process_command


EXIT_COMMANDS = [
    "goodbye",
    "good bye",
    "bye",
    "bye vexa",
    "stop listening",
    "stop listen",
    "sleep",
    "go to sleep",
    "going to sleep",
    "exit",
    "quit"
]

AUTO_SLEEP_TIME = 20


def start_vexa():

    print("===================================")
    print(" VisionControl AI - Vexa")
    print("===================================")

    while True:

        wait_for_vexa()

        print("\nVexa: I'm listening...")

        last_command_time = time.time()

        while True:

            if time.time() - last_command_time > AUTO_SLEEP_TIME:

                print("\nNo activity detected.")
                print("Vexa: Going to sleep...\n")

                break

            print("\nListening for command...")

            command = listen_command().lower().strip()

            if command == "":
                continue

            last_command_time = time.time()

            if any(exit_cmd in command for exit_cmd in EXIT_COMMANDS):

                print("\nVexa: Going to sleep...\n")

                break

            process_command(command)