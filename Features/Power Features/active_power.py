# Computes the active power of a power signal

import np as numpy

active_power=[]
for i in np.arange(len(power)):
    active_power.append(np.mean(power[i,:]))
    
active_power=np.array(active_power)

# power : vector containings power signals
