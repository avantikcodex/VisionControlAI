from brain.conversation.conversation_engine import ConversationEngine

engine = ConversationEngine()

print("=" * 50)
print("VEXA CONVERSATION TEST")
print("=" * 50)

while True:

    text = input("\nYou : ")

    if text.lower() == "exit":
        break

    reply = engine.reply(text)

    if reply:

        print("\nVexa :", reply)

    else:

        print("\nVexa : I'm still learning that.")