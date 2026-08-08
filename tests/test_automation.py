from automation.automation_engine import AutomationEngine


def main():

    engine = AutomationEngine()

    print("=" * 60)
    print("BROWSER AUTOMATION TEST")
    print("=" * 60)

    while True:

        website = input("\nWebsite : ").strip()

        if website.lower() == "exit":
            print("\nTest finished.")
            break

        if not website:
            continue

        engine.execute(
            "OPEN_WEBSITE",
            website
        )


if __name__ == "__main__":
    main()