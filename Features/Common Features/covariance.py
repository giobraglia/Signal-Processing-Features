# Calculates the covariance of voltage and current signals

import numpy as np

cov = []

for i in np.arange(len(current)):
    a = np.cov(current[i,0],voltage[i,0])
    a = a[0,1]
    cov.append(a)
    
cov = np.array(cov)

# current = vector containings current signals
# voltage = vector containings voltage signals

