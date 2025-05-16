import json
import importlib
import os
from task_guard import validate_task

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "task_registry.json")
MEMORY_PATH = os.path.join(os.path.dirname(__file__), "axiom_task_memory.json")

def load_registry():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return {}

def dispatch_task(task_name, *args, **kwargs):
    registry = load_registry()
    if task_name in registry:
        task = registry[task_name]
        module = importlib.import_module(f"axiomcore.{task['module']}")
        func = getattr(module, task["function"])
        return func(*args, **kwargs)

    memory = load_memory()
    if task_name in memory:
        task = memory[task_name]
        if validate_task(task):
            exec(task["code"], globals())
            return eval(f"{task['handler']}(*args, **kwargs)")
        else:
            raise PermissionError("Task validation failed.")

    raise ValueError(f"Task '{task_name}' not found in registry or memory.")
