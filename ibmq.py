#code for sending a program to ibmq

from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
from qiskit import QuantumCircuit, transpile

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token='yourtoken'
)

#print(my_backend)


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()

print(qc.draw())

my_backend = service.backend(name='ibm_sherbrooke')

qc = transpile(qc, my_backend)
print(qc.draw())

sampler = Sampler(mode=my_backend)
sampler.options.default_shots = 1024  # Options can be set using auto-complete.
job = sampler.run([qc])
print(f"Job ID is {job.job_id()}")
pub_result = job.result()[0]
print(f"Counts for the meas output register: {pub_result.data.meas.get_counts()}")


