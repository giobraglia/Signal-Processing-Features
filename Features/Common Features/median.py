# Computes the median of a signal, which is the value separating the higher half from the lower half of data samples

import numpy as np

median = []

for i in np.arange(len(power)):
    a = np.median(power[i,:])
    median.append(a)
    
median = np.array(median)

# power : vector containings power signals
