import speech_recognition as sr


def listen_command(device_index=None):

    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 80
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    recognizer.operation_timeout = None

    try:

        with sr.Microphone(device_index=device_index) as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Speak now...")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=5
            )

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You Said:", command)

        return command

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError as e:

        print("Speech Recognition Error:", e)
        return ""

    except Exception as e:

        print("Error:", e)
        return ""