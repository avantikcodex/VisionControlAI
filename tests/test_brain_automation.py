from brain.core.vexa_core import VexaCore


def main():

    core = VexaCore()

    print("=" * 60)
    print("VEXA BRAIN → AUTOMATION TEST")
    print("=" * 60)

    while True:

        sentence = input("\nYou : ").strip()

        if sentence.lower() in {
            "exit",
            "quit",
        }:
            print("\nVEXA : Test finished.")
            break

        if not sentence:
            continue

        request = core.execute(sentence)

        print("\nIntent :", request.intent)
        print("Entity :", request.entity)
        print("Decision :", request.decision)


if __name__ == "__main__":
    main()