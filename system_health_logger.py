# File: system_health_logger.py
import os
import psutil
from datetime import datetime

def log_system_health(log_file="system_health_log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    with open(log_file, "a") as f:
        f.write(f"{timestamp} | CPU: {cpu}% | RAM: {mem}%\n")

if __name__ == "__main__":
    log_system_health()
