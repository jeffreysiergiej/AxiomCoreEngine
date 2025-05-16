import json
import os
from .task_dispatcher import dispatch_task

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "task_registry.json")

def load_tasks():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)

def run_startup_tasks():
    tasks = load_tasks()
    for name, meta in tasks.items():
        if meta.get("trigger", {}).get("on_startup"):
            print(f"[STARTUP] Executing: {name}")
            dispatch_task(name)

def run_interval_tasks():
    # Placeholder: eventually handle threaded interval-based triggers
    pass
