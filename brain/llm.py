import requests

LLM_URL = "http://localhost:11434/api/generate"

def ask_jarvis(prompt: str) -> str:
    response = requests.post(
        LLM_URL,
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "I couldn't process that.")
