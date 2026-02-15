from brain.llm import ask_jarvis
from memory.memory import save_memory

class BaseAgent:
    def __init__(self, name="BaseAgent"):
        self.name = name

    def run_task(self, command):
        response = ask_jarvis(command)
        save_memory(command, response)
        return response
