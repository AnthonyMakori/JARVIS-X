import pyttsx3
import datetime
import threading

_engine = None
_engine_lock = threading.Lock()


def _init_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 175)
        _engine.setProperty("volume", 1.0)

        # Force female voice if available
        voices = _engine.getProperty("voices")
        for voice in voices:
            if "female" in voice.name.lower():
                _engine.setProperty("voice", voice.id)
                break
        else:
            if len(voices) > 1:
                _engine.setProperty("voice", voices[1].id)


def speak(text):
    global _engine
    with _engine_lock:
        if _engine is None:
            _init_engine()

        print(f"Jarvis: {text}")
        _engine.say(text)
        _engine.runAndWait()


def greet_user():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Good morning Sanny. How may I assist you today?"
    elif 12 <= hour < 17:
        greeting = "Good afternoon Sanny. What can I do for you?"
    elif 17 <= hour < 22:
        greeting = "Good evening Sanny. How can I help?"
    else:
        greeting = "Hello Sanny. How may I assist you?"

    speak(greeting)
