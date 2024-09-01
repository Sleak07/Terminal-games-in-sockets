"""the processed chunks are being made it into an audio file"""

# text_to_speech.py
# audio.py
import pyttsx3

class TextToSpeech:
    def __init__(self):
        # Initialize the pyttsx3 engine
        self.engine = pyttsx3.init()

    def speak(self, text: str):
        # Queue the text to be spoken
        self.engine.say(text)
        # Process the speech
        self.engine.runAndWait()

    def set_voice(self, voice_id: str):
        # Set the voice based on the provided voice ID
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voice_id)

    def set_rate(self, rate: int):
        # Set the speech rate (words per minute)
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume: float):
        # Set the volume level (0.0 to 1.0)
        self.engine.setProperty('volume', volume)
