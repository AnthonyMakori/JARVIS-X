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


def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)


def run_voice_loop():
    while True:
        command = listen_for_command()

        if command:
            print(f"You: {command}")
            response = agent.run_task(command)

            if response:
                speak(response)


if __name__ == "__main__":
    # Start API in background
    api_thread = threading.Thread(target=start_api)
    api_thread.daemon = True
    api_thread.start()

    # Run voice loop in main thread
    run_voice_loop()
