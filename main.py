# main.py – AxiomCoreEngine Launcher

from rlq_threader import initialize_rlq_thread
from rlq_memory_model import RLQMemoryModel
from ckm_engine import run_ckm_sim
from qpu_dispatcher import QPUSimulator

def main():
    print("\n=== AxiomCoreEngine Boot ===")

    # Step 1: RLQ Memory Core
    mem = RLQMemoryCore()
    mem.store("boot_status", {"ready": True})
    print("[RLQ] Memory initialized.")

    # Step 2: Launch CKM simulation
    print("\n[CKM] Running simulated knot field...")
    run_ckm_sim()

    # Step 3: Trigger QPU simulator
    print("\n[QPU] Simulating entanglement...")
    qpu = QPUSimulator()
    sample_input = "CKM-thread-A"
    output = qpu.process_input(sample_input)
    print("[QPU] Result:", output['entangled_state'])

    # Step 4: Thread test
    print("\n[RLQ] Threading logic...")
    thread = initialize_rlq_thread({"type": "diagnostic", "priority": 2})
    print("[RLQ] Thread started:", thread)

    print("\n=== System Ready ===")

if __name__ == "__main__":
    main()
