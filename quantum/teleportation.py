from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Function to create a Quantum Teleportation circuit
# Teleportation transfers the state of one qubit to another using entanglement
def create_teleportation():
    # Create a quantum circuit with 3 qubits and 3 classical bits
    # Qubit 0: State to be teleported (message qubit)
    # Qubit 1: First half of the entangled pair (Alice's qubit)
    # Qubit 2: Second half of the entangled pair (Bob's qubit)
    qc = QuantumCircuit(3, 3)
    
    # Create entanglement between qubit 1 and qubit 2
    qc.h(1)           # Apply Hadamard to qubit 1
    qc.cx(1, 2)       # Apply CNOT to entangle qubit 1 and qubit 2
    
    # Bell measurement on qubit 0 and qubit 1
    qc.cx(0, 1)       # Apply CNOT from qubit 0 to qubit 1
    qc.h(0)           # Apply Hadamard to qubit 0
    
    # Measure all three qubits
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

# Function to run the teleportation circuit on a simulator
def run_teleportation(qc):
    # Initialize the Aer simulator
    simulator = AerSimulator()
    # Run the circuit 1024 times and get the results
    result = simulator.run(qc, shots=1024).result()
    # Return the measurement counts
    return result.get_counts()