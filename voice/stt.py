import pvporcupine
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from dotenv import load_dotenv
import queue
import os


load_dotenv()
access_key = os.getenv("PICOVOICE_ACCESS_KEY")
# Use lightweight whisper
model = WhisperModel("tiny", compute_type="int8")

print("Access Key Loaded:", access_key)

# Initialize Porcupine
porcupine = pvporcupine.create(
    access_key=access_key,
    keywords=["jarvis"]
)
q = queue.Queue()

def audio_callback(indata, frames, time, status):
    q.put(indata.copy())

def listen_for_command():
    print("Listening for wake word...")

    with sd.InputStream(
        samplerate=porcupine.sample_rate,
        channels=1,
        dtype="int16",
        blocksize=porcupine.frame_length,
        callback=audio_callback,
    ):
        while True:
            pcm = q.get()
            pcm = pcm.flatten()

            result = porcupine.process(pcm)

            if result >= 0:
                print("Wake word detected!")
                return record_command()

def record_command():
    print("Listening for command...")

    duration = 5  # seconds
    audio = sd.rec(
        int(16000 * duration),
        samplerate=16000,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    # 🔥 IMPORTANT FIX
    audio = np.squeeze(audio)  

    segments, _ = model.transcribe(
        audio,
        beam_size=1,
        language="en"   
    )

    text = " ".join([segment.text for segment in segments])

    print("Recognized:", text)
    return text

