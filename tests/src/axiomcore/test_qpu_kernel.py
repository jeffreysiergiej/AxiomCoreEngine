import numpy as np
from src.axiomcore.qpu_kernel import apply_quantum_gate, hadamard, identity, quantum_superposition

def test_apply_quantum_gate():
    state = np.array([1, 0])
    gate = identity()
    result = apply_quantum_gate(state, gate)
    assert np.array_equal(result, state)

def test_hadamard_output():
    h = hadamard()
    expected = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    assert np.allclose(h, expected)

def test_quantum_superposition():
    superposed = quantum_superposition()
    expected = np.array([1, 1])  # normalized after Hadamard
    assert np.allclose(superposed, expected)
