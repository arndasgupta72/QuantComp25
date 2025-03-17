import matplotlib.pyplot as plt
import numpy as np
import math
#import cmatrix

from qiskit_aer import  AerSimulator
from qiskit import transpile
from qiskit import assemble
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

from qiskit.visualization import plot_histogram

qhc=QuantumCircuit(4,2)

#build b
#for i in range(3):
qhc.x(0)
#qhc.h(0)

#qpe

qhc.h(1)
qhc.h(2)

qhc.barrier(0,1,2,3)


qhc.cu(math.pi,math.pi,0,0,1,0)
qhc.cu(math.pi/2,-math.pi/2,math.pi/2,0.75*math.pi,2,0)

qhc.barrier(0,1,2,3)

#iqft

qhc.h(1)
qhc.cp(-math.pi/2,1,2)
qhc.h(2)

qhc.swap(1,2)
qhc.barrier(0,1,2,3)


#rotation
qhc.cry(math.pi/3,2,3)
qhc.cry(math.pi,1,3)

#qhc.barrier(3)

#measurement
#qhc.measure(3,0)

qhc.barrier(0,1,2,3)

#qft
qhc.swap(1,2)
qhc.h(2)
qhc.cp(math.pi/2,1,2)
qhc.h(1)

#qhc.barrier(3)
qhc.barrier(0,1,2,3)


#uncompute
qhc.cu(math.pi/2,math.pi/2,-math.pi/2,-0.75*math.pi,2,0)
qhc.cu(math.pi,math.pi,0,0,1,0)

qhc.barrier(0,1,2,3)

qhc.h(1)
qhc.h(2)

qhc.measure(3,0)

qhc.measure(0,0)
#qhc.measure_all(inplace=False)

qhc.draw("mpl")
plt.show()
aersim=AerSimulator()
qhc_measured = qhc.measure_all(inplace=False)

from qiskit.primitives import StatevectorSampler
sampler=StatevectorSampler()
#result = StatevectorSampler().run([qhc],shots=10000).result()
job=sampler.run([qhc_measured],shots=10000)
result= job.result()

print(f" > Counts: {result[0].data.meas.get_counts()}")
counts_ideal=result[0].data.meas.get_counts()


plot_histogram(counts_ideal)
plt.show()


#print(f"Count data:\n {result[0].data.c.get_int_counts()}")

#counts_ideal=result[0].data.c.get_int_counts()

#plot_histogram(counts_ideal)
#plt.show()






