from voice.voice_engine import VoiceEngine

voice = VoiceEngine()

print("=" * 60)
print("VOICE ENGINE TEST")
print("=" * 60)

while True:

    sentence = voice.listen()

    if sentence.lower() == "exit":
        break

    if voice.wake(sentence):

        voice.speak("Yes, I am listening.")

    else:

        print("Wake word not detected.")