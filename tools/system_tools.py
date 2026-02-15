import os
import psutil

def open_app(app_name: str):
    os.system(f"start {app_name}")

def get_system_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return f"CPU usage is {cpu}% and RAM usage is {ram}%."
