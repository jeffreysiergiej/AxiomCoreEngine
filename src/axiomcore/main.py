from qpu_interface import receive_memory_dump
from dotenv import load_dotenv
load_dotenv()

import os
print("PYTHONPATH is set to:", os.getenv("PYTHONPATH"))

from genesis_ai import genesis_daemon
from rlq_memory_model import RLQMemoryModel
from auto_commit_logger import start_commit_loop

def main():
    print("=== AxiomCoreEngine Boot ===")

    # Launch Genesis daemon
    genesis_daemon()

    # Initialize memory core
    mem = RLQMemoryModel()
    mem.update("anchor_event", {"score": 0.92, "timestamp": 123456789})
    print("Recalled:", mem.recall("anchor_event"))

    # Export memory and send to QPU
    receive_memory_dump(mem.export_state())

    # Start auto-commit loop
    start_commit_loop()

if __name__ == "__main__":
    main()
from system_health_logger import run_health_daemon
import threading

# Launch background system health logging
health_thread = threading.Thread(target=run_health_daemon, daemon=True)
health_thread.start()
