import json
import importlib
import os

# Load task registry JSON
def load_task_registry():
    with open("task_registry.json", "r") as f:
        return json.load(f)

# Dispatch task by name
def dispatch_task(task_name, **kwargs):
    registry = load_task_registry()
    task_info = registry.get(task_name)

    if not task_info:
        print(f"[ERROR] Task '{task_name}' not found.")
        return

    handler_name = task_info["handler"]
    
    # Dynamically resolve the handler function
    try:
        handler_func = globals().get(handler_name)
        if not handler_func:
            module_name = task_info.get("module", "system_health_logger")
            module = importlib.import_module(module_name)
            handler_func = getattr(module, handler_name)
        handler_func(**kwargs)
    except Exception as e:
        print(f"[DISPATCH ERROR] Failed to run task '{task_name}':", e)
