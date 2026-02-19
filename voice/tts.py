import pyttsx3
import datetime

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

# 🔥 Force female voice
voices = engine.getProperty("voices")
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break
else:
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


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
