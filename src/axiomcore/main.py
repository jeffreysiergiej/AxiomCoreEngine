from qpu_interface import receive_memory_dump
from dotenv import load_dotenv
load_dotenv()

import os
import sys
from genesis_ai import genesis_daemon
from rlq_memory_model import RLQMemoryModel
from auto_commit_logger import start_commit_loop
from system_health_logger import run_health_daemon
import threading

# Setup unified runtime log
log_path = "system_runtime.log"
sys.stdout = open(log_path, "a")
sys.stderr = sys.stdout

def main():
    print("=== AxiomCoreEngine Boot ===")
    print("PYTHONPATH is set to:", os.getenv("PYTHONPATH"))

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
    # Start system health monitoring in background
    health_thread = threading.Thread(target=run_health_daemon, daemon=True)
    health_thread.start()

    # Boot main runtime
    main()
