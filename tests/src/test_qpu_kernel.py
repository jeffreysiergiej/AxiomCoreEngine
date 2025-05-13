from src.axiomcore.qpu_kernel import quantum_superposition
import numpy as np

def test_quantum_superposition():
    result = quantum_superposition()
    expected = np.array([1, 1]) / np.sqrt(2)
    assert np.allclose(result, expected)
