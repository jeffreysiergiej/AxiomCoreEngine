import numpy as np

def apply_quantum_gate(state, gate):
    """Apply a quantum gate to a state vector."""
    return np.dot(gate, state)

def hadamard():
    """Hadamard gate."""
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def identity():
    return np.eye(2)

def quantum_superposition():
    """Return a qubit in superposition."""
    return np.dot(hadamard(), np.array([1, 0]))
