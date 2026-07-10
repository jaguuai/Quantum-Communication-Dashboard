from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Function to create a Quantum Entanglement circuit
# This demonstrates the correlation between two entangled qubits
def create_entanglement():
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    # Apply Hadamard gate to qubit 0 for superposition
    qc.h(0)
    # Apply CNOT gate to create entanglement between qubits
    qc.cx(0, 1)
    # Measure both qubits and store results in classical bits
    qc.measure([0, 1], [0, 1])
    return qc

# Function to run the entanglement circuit on a simulator
def run_entanglement(qc):
    # Initialize the Aer simulator
    simulator = AerSimulator()
    # Run the circuit 1024 times and get the results
    result = simulator.run(qc, shots=1024).result()
    # Return the measurement counts
    return result.get_counts()