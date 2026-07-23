from voice.speech_recognition import listen_command


def wait_for_vexa():

    print("Waiting for Vexa...")

    while True:

        command = listen_command()

        if command == "":
            continue

        print("Heard:", command)

        if (
            "vexa" in command
            or "hey vexa" in command
            or "hey alexa" in command
            or "alexa" in command
            or "axea" in command
        ):

            print("Vexa Activated")

            return True