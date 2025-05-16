import json
import importlib
import os

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "task_registry.json")

def load_registry():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)

def dispatch_task(task_name, *args, **kwargs):
    registry = load_registry()
    if task_name not in registry:
        raise ValueError(f"Task '{task_name}' not found in registry.")

    task = registry[task_name]
    module = importlib.import_module(f"axiomcore.{task['module']}")
    func = getattr(module, task["function"])
    return func(*args, **kwargs)
