from .qpu_kernel import quantum_superposition
from .os_kernel import AxiomOSKernel

def handle_qpc(command: str):
    """Basic QPU command protocol."""
    kernel = AxiomOSKernel()

    if command == "INIT_SUPERPOSITION":
        kernel.schedule_task(lambda: print(quantum_superposition()))
    elif command == "PING":
        kernel.schedule_task(lambda: print("ACK"))
    else:
        kernel.schedule_task(lambda: print("UNKNOWN_CMD"))

    kernel.run_all()
