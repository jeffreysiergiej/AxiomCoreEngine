# test_rlq_thread.py

from rlq_threader import initialize_rlq_thread
from rlq_memory_model import RLQMemoryCore

# Sample state to initialize thread with
sample_state = {
    "id": "test_001",
    "priority": 3,
    "context": "Diagnostics",
    "steps": ["init", "analyze", "report"]
}

# Initialize memory core and run thread
memory_core = RLQMemoryCore()
thread_result = initialize_rlq_thread(sample_state)

print("RLQ Thread Initialized:")
print(thread_result)
