import sys
import pennylane as qml
from pennylane import numpy as np


def deutsch_jozsa(oracle):
    """This function will determine whether an oracle defined by a function f is constant or balanced.

    Args:
        - oracle (function): Encoding of the f function as a quantum gate. The first two qubits refer to the input and the third to the output.

    Returns:
        - (str): "constant" or "balanced"
    """

    dev = qml.device("default.qubit", wires=3, shots=1)

    @qml.qnode(dev)
    def circuit():
        """Implements the Deutsch Jozsa algorithm."""

        # QHACK #

        qml.Hadamard(0)
        qml.Hadamard(1)
        qml.PauliX(2)
        qml.Hadamard(2)

        oracle()  # DO NOT MODIFY this line

        qml.Hadamard(0)
        qml.Hadamard(1)

        # QHACK #

        return qml.sample(wires=range(2))

    # QHACK #

    # From `sample` (a single call to the circuit), determine whether the function is constant or balanced.
    
    val = circuit()
    print(val)
    if val.sum() == 0:
        return 'balanced'
    else:
        return 'constant'

    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    numbers = [int(i) for i in inputs]

    def oracle():
        for i in numbers:
            qml.CNOT(wires=[i, 2])

    output = deutsch_jozsa(oracle)
    print(output)
