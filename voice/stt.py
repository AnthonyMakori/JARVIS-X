import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import pyttsx3

engine = pyttsx3.init()
model = WhisperModel("small")  # light CPU model

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_wake_word():
    print("Listening for wake word...")
    while True:
        audio = sd.rec(int(16000 * 2), samplerate=16000, channels=1)
        sd.wait()
        audio_np = audio.flatten().astype(np.float32)
        segments, _ = model.transcribe(audio_np)
        for segment in segments:
            if "jarvis" in segment.text.lower():
                print("Wake word detected!")
                speak("Yes?")
                return  # proceed to recording command

listen_for_wake_word()
