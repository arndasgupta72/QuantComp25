
#Qiskit modules

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram, plot_state_city


#Qiskit backend

from qiskit_aer import  AerSimulator
from qiskit import transpile
from qiskit import assemble
from qiskit_aer import Aer
#python packages

import matplotlib.pyplot as plt
import numpy as np
import math

q=QuantumRegister(2,'q')
c=ClassicalRegister(2,'c')
grover = QuantumCircuit(q,c)
grover.h(q[0])
grover.h(q[1])
grover.cz(q[0], q[1])
grover.h(q[0])
grover.h(q[1])
grover.z(q[0])
grover.z(q[1])
grover.cz(q[0],q[1])
grover.h(q[0])
grover.h(q[1])

grover.draw("mpl")
plt.show()



simulator=Aer.get_backend('unitary_simulator')
result1=simulator.run(grover).result()
unitary=result1.get_unitary(grover)
print("Circuit unitary:\n", unitary)




simulator=Aer.get_backend('statevector_simulator')
result1=simulator.run(grover).result()
statevector=result1.get_statevector(grover)
plot_state_city(statevector, title='Grover State')
plt.show()


grover_measured = grover.measure_all(inplace=False)


from qiskit.primitives import StatevectorSampler
sampler=StatevectorSampler()
job=sampler.run([grover_measured],shots=1000)
result= job.result()
print(f" > Counts: {result[0].data["meas"].get_counts()}")
counts_ideal=result[0].data["meas"].get_counts()


plot_histogram(counts_ideal)
plt.show()




