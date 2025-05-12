# === AxiomCoreEngine Boot ===

from rlq_memory_model import RLQMemoryModel

def main():
    print("=== AxiomCoreEngine Boot ===")

    # Initialize memory core
    mem = RLQMemoryModel()

    # Example use
    mem.update("anchor_event", {"score": 0.92, "timestamp": 12437})
    print("Recalled:", mem.recall("anchor_event"))

if __name__ == "__main__":
    main()
