from voice.wake_word import wait_for_vexa
from voice.speech_recognition import listen_command
from voice.command_parser import process_command

print("Starting Vexa...")

wait_for_vexa()

print("Listening for command...")

command = listen_command()

process_command(command)