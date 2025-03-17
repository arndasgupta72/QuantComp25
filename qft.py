#initialization
import matplotlib.pyplot as plt
import numpy as np
import math

# importing Qiskit
#from qiskit import Aer, transpile, assemble
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

from qiskit_aer import  AerSimulator
from qiskit import transpile
from qiskit import assemble
from qiskit_aer import Aer



# import basic plot tools and circuits
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT

qpe = QuantumCircuit(4, 3)
qpe.x(3)
qpe.draw()

for qubit in range(3):
    qpe.h(qubit)
qpe.draw()

repetitions = 1
for counting_qubit in range(3):
    for i in range(repetitions):
        qpe.cp(math.pi/(4.5), counting_qubit, 3); # controlled-T
    repetitions *= 2
qpe.draw()

qpe.barrier()
# Apply inverse QFT
qpe = qpe.compose(QFT(3, inverse=True), [0,1,2])
# Measure
qpe.barrier()
for n in range(3):
    qpe.measure(n,n)

qpe.draw()

aersim=AerSimulator()
qpe_measured = qpe.measure_all(inplace=False)

from qiskit.primitives import StatevectorSampler
sampler=StatevectorSampler()
#sampler = Sampler(mode=backend)
#sampler.options.default_shots = 10_000
#result = sampler.run([qpe]).result()
job=sampler.run([qpe_measured],shots=1000)
result= job.result()
#dist = result[0].data.meas.get_counts()


#job=sampler.run([qpe_measured],shots=1000)
#result= job.result()
print(f" > Counts: {result[0].data.meas.get_counts()}")
counts_ideal=result[0].data.meas.get_counts()


plot_histogram(counts_ideal)
plt.show()
