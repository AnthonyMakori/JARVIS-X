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
            response = agent.run_task(command)
            speak(response)

if __name__ == "__main__":
    # Start FastAPI in a separate thread
    api_thread = threading.Thread(target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000, reload=False))
    api_thread.start()

    # Run voice loop on main thread (important for mic)
    run_voice_loop()
