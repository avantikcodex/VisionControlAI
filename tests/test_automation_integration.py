from automation.automation_engine import AutomationEngine


def main():

    engine = AutomationEngine()

    print("=" * 60)
    print("AUTOMATION ENGINE INTEGRATION TEST")
    print("=" * 60)

    # ---------------------------------------------------------
    # APPLICATION
    # ---------------------------------------------------------

    print("\n[1] Opening Notepad...")

    engine.execute(
        "OPEN_APPLICATION",
        "notepad"
    )

    engine.keyboard.wait(2)

    # ---------------------------------------------------------
    # KEYBOARD
    # ---------------------------------------------------------

    print("\n[2] Typing text...")

    engine.execute(
        "TYPE_TEXT",
        "Hello from VEXA Automation!"
    )

    engine.execute(
        "ENTER"
    )

    engine.execute(
        "TYPE_TEXT",
        "VisionControl AI is controlling Windows."
    )

    engine.execute(
        "ENTER"
    )

    # ---------------------------------------------------------
    # KEYBOARD SHORTCUT
    # ---------------------------------------------------------

    print("\n[3] Testing keyboard shortcut...")

    engine.execute(
        "TYPE_TEXT",
        "This line will be selected."
    )

    engine.execute(
        "SELECT_ALL"
    )

    engine.keyboard.wait(1)

    engine.execute(
        "COPY"
    )

    engine.keyboard.wait(1)

    engine.execute(
        "PASTE"
    )

    # ---------------------------------------------------------
    # MOUSE
    # ---------------------------------------------------------

    print("\n[4] Testing mouse...")

    width, height = engine.mouse.screen_size()

    if width and height:

        engine.execute(
            "MOUSE_MOVE",
            [
                width // 2,
                height // 2
            ]
        )

    # ---------------------------------------------------------
    # BROWSER
    # ---------------------------------------------------------

    print("\n[5] Testing browser...")

    engine.execute(
        "OPEN_WEBSITE",
        "https://www.google.com"
    )

    print("\n" + "=" * 60)
    print("AUTOMATION INTEGRATION TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()