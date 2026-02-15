from fastapi import APIRouter
from brain.llm import ask_jarvis
from tools.system_tools import open_app, get_system_stats

router = APIRouter()

@router.get("/")
def home():
    return {"message": "JARVIS is online."}

@router.post("/command")
def execute_command(command: str):
    cmd = command.lower()
    
    if "open chrome" in cmd:
        open_app("chrome")
        return {"response": "Opening Chrome."}
    
    if "system status" in cmd:
        stats = get_system_stats()
        return {"response": stats}

    response = ask_jarvis(command)
    return {"response": response}
