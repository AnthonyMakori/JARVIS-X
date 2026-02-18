import threading
import uvicorn
from fastapi import FastAPI
from api.routes import router
from voice.stt import listen_for_command
from voice.tts import speak
from agents.base_agent import BaseAgent

app = FastAPI(title="JARVIS-X")
app.include_router(router)

agent = BaseAgent("Jarvis")


def run_voice_loop():
    speak("Jarvis online and ready.")

    while True:
        command = listen_for_command()

        if command:
            print(f"You: {command}")

            # Make it conversational
            response = agent.run_task(command)

            speak(response)


if __name__ == "__main__":
    # Run voice loop in background
    voice_thread = threading.Thread(target=run_voice_loop, daemon=True)
    voice_thread.start()

    # Run FastAPI WITHOUT reload to prevent duplicate threads
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
