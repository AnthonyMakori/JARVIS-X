import requests

LLM_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Jarvis, a smart, concise AI assistant.
Speak like Siri.
Be short, natural, and conversational.
Never give long essays.
Maximum 2 sentences unless the user explicitly asks for a detailed explanation.
If the user asks to open an app, do not explain how — just acknowledge.
"""

def ask_jarvis(prompt: str) -> str:
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}\nJarvis:"

    try:
        response = requests.post(
            LLM_URL,
            json={
                "model": "mistral",
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.6,
                    "num_predict": 120  # limits length
                }
            }
        )

        result = response.json().get("response", "").strip()

        # Extra safety trim (prevents long outputs)
        result = result.split("\n")[0]

        if not result:
            return "I'm not sure how to respond to that."

        return result

    except Exception:
        return "I'm having trouble connecting to my language model."
