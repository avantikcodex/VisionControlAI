from voice.microphone import Microphone
from voice.recorder import Recorder
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech
from voice.wake_word import detected


class VoiceEngine:

    def __init__(self):

        self.microphone = Microphone()

        self.recorder = Recorder()

        self.stt = SpeechToText()

        self.tts = TextToSpeech()

    def listen(self):

        self.microphone.start()

        audio = self.recorder.record()

        sentence = self.stt.convert(audio)

        self.microphone.stop()

        return sentence

    def wake(self, sentence):

        return detected(sentence)

    def speak(self, text):

        self.tts.speak(text)    