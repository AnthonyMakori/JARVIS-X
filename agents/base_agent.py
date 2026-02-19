import subprocess
from brain.llm import ask_jarvis
from memory.memory import save_memory


class BaseAgent:
    def __init__(self, name="Jarvis"):
        self.name = name

    def run_task(self, command):
        command_lower = command.lower()

        # 🔥 Real System Commands First
        if "open chrome" in command_lower:
            try:
                subprocess.Popen(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                )
                response = "Opening Chrome."
            except Exception:
                response = "I couldn't find Chrome installed."
            
            save_memory(command, response)
            return response

        if "open notepad" in command_lower:
            subprocess.Popen("notepad.exe")
            response = "Opening Notepad."
            save_memory(command, response)
            return response

        # 🔥 Otherwise use LLM (short assistant style)
        response = ask_jarvis(command)

        save_memory(command, response)
        return response
