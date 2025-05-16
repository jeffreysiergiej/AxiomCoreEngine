# AxiomCoreEngine – Phase 2 Upgrade: Expansion Layer

This upgrade introduces dynamic task expansion capabilities, allowing the system to learn, store, validate, and execute new functions at runtime.

---

## Core Additions

### 1. `axiom_task_memory.json`
- **Purpose:** Stores dynamically learned tasks.
- **Format:**
  ```json
  {
    "learned_tasks": [
      {
        "name": "new_task_name",
        "description": "What this task does.",
        "code": "def new_task_name(): print('Dynamic task executed!')"
      }
    ]
  }

  
⸻

2. task_learner.py
	•	Function: learn_task(name, description, code)
	•	Behavior: Appends a new task definition to axiom_task_memory.json.

⸻

3. task_guard.py
	•	Function: validate_task(task_dict)
	•	Behavior: Performs basic safety validation before a dynamic task is executed.
	•	Future Scope: Extend to restrict unsafe imports or unauthorized operations.

⸻

4. task_dispatcher.py (Updated)
	•	Searches:
	1.	First: task_registry.json
	2.	Second: axiom_task_memory.json
	•	If task is found dynamically and validated, it is executed at runtime via exec() and eval().

⸻

Example: How to Add a New Dynamic Task


from axiomcore.task_learner import learn_task

code = """
def greet_dynamic(name="Friend"):
    print(f"Hello, {name} — this is a learned task.")
    return f"Greeted {name}"
"""

learn_task("greet_dynamic", "Greets dynamically", code)


Then call it:


from axiomcore.task_dispatcher import dispatch_task

dispatch_task("greet_dynamic", name="Jeff")


Logs and Safety
	•	Logs are still written via system_runtime.log and system_health.log.
	•	All learned tasks pass through task_guard.py before execution.

⸻

Next Phase: task_memory_upgrade.py
	•	Reinforce persistent, versioned task storage
	•	Add rollback history and confidence scores for learned behaviors

⸻

Author: Jeffrey Siergiej
Last Updated: Phase 2 Completion
