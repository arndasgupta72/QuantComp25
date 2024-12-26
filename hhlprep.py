import matplotlib.pyplot as plt
import numpy as np
import math
import cmatrix


from qiskit_aer import  AerSimulator
from qiskit import transpile
from qiskit import assemble
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

from qiskit.visualization import plot_histogram

qhc=QuantumCircuit(4,1)

#build b
for i in range(3):
 qhc.x(i)

#qpe

qhc.h(1)
qhc.h(2)

qhc.barrier(0,1,2,3)


qhc.cu(cmatrix.theta,cmatrix.phi1,cmatrix.phi2,cmatrix.gamma,2,0)
qhc.cu(cmatrix.theta,cmatrix.phi1,cmatrix.phi2,cmatrix.gamma,1,0)
qhc.cu(cmatrix.theta,cmatrix.phi1,cmatrix.phi2,cmatrix.gamma,1,0)

qhc.barrier(0,1,2,3)

#iqft

qhc.h(1)
qhc.cp(-math.pi/2,1,2)
qhc.h(2)

qhc.swap(1,2)
qhc.barrier(0,1,2,3)


#rotation
qhc.cry(cmatrix.xi2,1,3)
qhc.cry(cmatrix.xi1,2,3)

#qhc.barrier(3)

#measurement
qhc.measure(3,0)

qhc.barrier(0,1,2,3)

#qft
qhc.swap(1,2)
qhc.h(2)
qhc.cp(math.pi/2,1,2)
qhc.h(1)

#qhc.barrier(3)
qhc.barrier(0,1,2,3)


#uncompute
qhc.cu(cmatrix.theta12,cmatrix.rho1,cmatrix.rho2,cmatrix.gamma12,1,0)
qhc.cu(cmatrix.theta,cmatrix.phi1,cmatrix.phi2,cmatrix.gamma,2,0)
qhc.cu(cmatrix.theta,cmatrix.phi1,cmatrix.phi2,cmatrix.gamma,2,0)

qhc.barrier(0,1,2,3)

#qhc.h(1)
#qhc.h(2)

qhc.measure(0,0)

qhc.draw("mpl")
plt.show()

aersim=AerSimulator()
shots=100000
t_qhc=transpile(qhc,aersim)
qobj = assemble(t_qhc, shots=shots)
result_ideal=aersim.run(qobj).result()
counts_ideal=result_ideal.get_counts(0)
    
plot_histogram(counts_ideal)
plt.show()

