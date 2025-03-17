
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

q=QuantumRegister(3,'q')
c=ClassicalRegister(2,'c')
circ = QuantumCircuit(q,c)
circ.h(q[0])
circ.cx(q[0],q[1])
circ.h(q[0])
circ.cx(q[1], q[2])
circ.measure(q[0],c[0])
circ.measure(q[1],c[1])

circ.draw("mpl")
plt.show()

simulator=Aer.get_backend('statevector_simulator')
result1=simulator.run(circ).result()
statevector=result1.get_statevector(circ)
plot_state_city(statevector, title='Bob state')
plt.show()





