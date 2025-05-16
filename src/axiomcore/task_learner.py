import json
import os

MEMORY_PATH = os.path.join(os.path.dirname(__file__), "axiom_task_memory.json")

def learn_task(name, description, code):
    print(f"[LEARN] Registering new task: {name}")
    task_entry = {
        "name": name,
        "description": description,
        "code": code,
    }

    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            data = json.load(f)
    else:
        data = {"learned_tasks": []}

    data["learned_tasks"].append(task_entry)

    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=2)

    return True
