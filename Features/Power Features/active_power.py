# Computes the active power of a power signal
# The active power is simply calculated by taking the dc value of the power signal

import np as numpy

P = []
for i in np.arange(len(power)):
    P.append(np.mean(power[i,:]))
    
P = np.array(P)

# power : vector containings power signals
