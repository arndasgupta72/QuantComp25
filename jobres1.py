
#Code for retrieving results from the IBM Q (completed)
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
 
service = QiskitRuntimeService(
     channel='ibm_quantum',
     instance='ibm-q/open/main',
 token='yourtoken' )
job = service.job('jobid')
job_result = job.result()

pub_result = job_result[0].data.meas.get_counts() 
print(f" > Counts: {job_result[0].data.meas.get_counts()}") #classicalregister= meas

plot_histogram(pub_result)
plt.show()
