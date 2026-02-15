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
    while True:
        command = listen_for_command()
        if command:
            print(f"You: {command}")
            response = agent.run_task(command)
            print(f"Jarvis: {response}")
            speak(response)

if __name__ == "__main__":
    import threading
    # Run voice loop in background
    threading.Thread(target=run_voice_loop, daemon=True).start()
    # Run FastAPI
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
