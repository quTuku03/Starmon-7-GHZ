# 7-Qubit-GHZ-Entanglement-on-Starmon-7

This project demonstrates **multipartite quantum entanglement** by generating a Greenberger-Horne-Zeilinger (GHZ) state on the Starmon-7 quantum processor.

##  The Physics
We create a state where 7 qubits are entangled such that they are all in the $|0\rangle$ state OR all in the $|1\rangle$ state simultaneously, with no overlap.

The ket state is:

$$|\text{GHZ}\rangle = \frac{|0000000\rangle + |1111111\rangle}{\sqrt{2}}$$

### What to Expect
1.  **Ideal Scenario:** We measure `0000000` 50% of the time and `1111111` 50% of the time.
2.  **Real Hardware:** Due to noise (decoherence and readout errors), you will see other states (like `0000001` or `1000000`). The contrast between the target states and the noise indicates the quality of the quantum processor.

## Usefull links
* https://www.quantum-inspire.com/
* https://github.com/DiCarloLab-Delft/QuantumInspireUtilities
* https://github.com/QuTech-Delft/quantuminspire2

## Prerequisites
* Python 3.8+
* `qiskit`
* `qiskit-quantuminspire`
* `matplotlib`

##  How to Run
Create a jupyter notebook and enter the following
1. !qi login "https://api.quantum-inspire.com"
2. provider = QIProvider()
3. provider.backends()
4. backend_name = "Starmon-7"
backend = provider.get_backend(name=backend_name)
5. %matplotlib inline
%run GHZ_test.py 
