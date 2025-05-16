import json
import os

MEMORY_PATH = os.path.join(os.path.dirname(__file__), "axiom_task_memory.json")

def learn_task(name, description, code, handler):
    new_task = {
        "description": description,
        "handler": handler,
        "code": code
    }

    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            memory = json.load(f)
    else:
        memory = {}

    memory[name] = new_task

    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"Learned new task: {name}")
