from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_quantuminspire.qi_provider import QIProvider

# Setup Quantum Inspire
provider = QIProvider()
backend = provider.get_backend("Starmon-7")

# Creates a 7-qubit GHZ circuit
qc = QuantumCircuit(7, 7)
qc.h(0)
for i in range(6):
    qc.cx(i, i+1)
qc.measure(range(7), range(7))

# Circuit diagram
print("GHZ Circuit:")
print(qc.draw(output='text'))
qc.draw(output='mpl')
plt.title("7-qubit GHZ Circuit")
plt.show()

# Quantum backend
transpiled_qc = transpile(qc, backend=backend)
job = backend.run(transpiled_qc, shots=1024)
result = job.result()
counts = result.get_counts()

# Prints probabilities for each state
print("\nMeasurement results (1024 shots):")
for state, count in sorted(counts.items()):
    probability = count / 1024
    print(f"State |{state}⟩: {count} counts ({probability:.3f})")

# Histogram
plot_histogram(counts)
plt.title("GHZ State Measurement Probabilities")
plt.show()
