from dotenv import load_dotenv
load_dotenv()

import os
print("PYTHONPATH is set to:", os.getenv("PYTHONPATH"))

from genesis_ai import genesis_daemon
from rlq_memory_model import RLQMemoryModel
from auto_commit_logger import start_commit_loop

def main():
    print("=== AxiomCoreEngine Boot ===")
    ...
