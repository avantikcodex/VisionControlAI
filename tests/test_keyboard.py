from automation.keyboard_controller import KeyboardController
import subprocess


def main():

    keyboard = KeyboardController()

    print("=" * 60)
    print("KEYBOARD SHORTCUT TEST")
    print("=" * 60)

    print("\nOpening Notepad...")

    subprocess.Popen(["notepad.exe"])

    keyboard.wait(2)

    keyboard.type_text("VEXA Keyboard Test")

    keyboard.press("enter")

    keyboard.type_text("Testing Ctrl+A")

    keyboard.press("enter")

    keyboard.type_text("Testing Ctrl+C")

    keyboard.press("enter")

    keyboard.type_text("Testing Ctrl+V")

    keyboard.press("enter")

    print("\nTesting Ctrl+A...")

    keyboard.select_all()

    keyboard.wait(1)

    print("Ctrl+A completed.")

    print("\nTesting Ctrl+C...")

    keyboard.copy()

    keyboard.wait(1)

    print("Ctrl+C completed.")

    print("\nTesting Ctrl+V...")

    keyboard.paste()

    keyboard.wait(1)

    print("Ctrl+V completed.")

    print("\nKEYBOARD TEST FINISHED")


if __name__ == "__main__":
    main()