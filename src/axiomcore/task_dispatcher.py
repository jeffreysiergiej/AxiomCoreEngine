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

from .task_guard import validate_task

DYNAMIC_MEMORY_PATH = os.path.join(os.path.dirname(__file__), "axiom_task_memory.json")

def dispatch_task(task_name, *args, **kwargs):
    registry = load_registry()
    if task_name in registry:
        task = registry[task_name]
        module = importlib.import_module(f"axiomcore.{task['module']}")
        func = getattr(module, task["function"])
        return func(*args, **kwargs)

# Try dynamic memory
    if os.path.exists(DYNAMIC_MEMORY_PATH):
        with open(DYNAMIC_MEMORY_PATH, "r") as f:
            dynamic_tasks = json.load(f).get("learned_tasks", [])
        for task in dynamic_tasks:
            if task["name"] == task_name and validate_task(task):
                exec(task["code"], globals())
                return eval(f"{task_name}(*args, **kwargs)")

    raise ValueError(f"Task '{task_name}' not found in registry or dynamic memory.")
