import matplotlib.pyplot as plt
import numpy as np
import math

from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit import assemble
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

from qiskit.visualization import plot_histogram

#Input the number A

q = QuantumRegister(5,'q')
c = ClassicalRegister(2,'c')
circuit = QuantumCircuit(q,c)
circuit.x(q[0])
circuit.cx(q[0],q[3])
circuit.cx(q[1],q[3])
circuit.cx(q[2],q[3])
circuit.ccx(q[0],q[1],q[4])
circuit.ccx(q[0],q[2],q[4])
circuit.ccx(q[1],q[2],q[4])
circuit.measure(q[3],c[0])
circuit.measure(q[4],c[1])

circuit.draw("mpl")
plt.show()

aersim=AerSimulator()
shots=100000
t_circ=transpile(circuit,aersim)
qobj = assemble(t_circ, shots=shots)
result_ideal=aersim.run(qobj).result()
counts_ideal=result_ideal.get_counts(0)

print(counts_ideal)

plot_histogram(counts_ideal)
plt.show()


#Input the number B
