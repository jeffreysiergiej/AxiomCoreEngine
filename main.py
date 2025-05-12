from genesis_ai import genesis_daemon
from rlq_memory_model import RLQMemoryModel
from auto_commit_logger import start_commit_loop

def main():
    print("=== AxiomCoreEngine Boot ===")
    
    # Launch Genesis daemon to evaluate agent triggers
    genesis_daemon()
    
    # Initialize memory core
    mem = RLQMemoryModel()
    
    # Example use
    mem.update("anchor_event", {"score": 0.92, "timestamp": 12437})
    print("Recalled:", mem.recall("anchor_event"))
    
    # Start GitHub auto-commit loop
    start_commit_loop()

if __name__ == "__main__":
    main()
