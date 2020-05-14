# Calculates the apparent power of a signal
# First the root mean square value of the current and voltage signals is computed,
# then the apparent power is calculated as S = Irms * Vrms

import numpy as np

Irms = []
Vrms = []

for i in np.arange(len(current)):
    rmsi = np.sqrt(np.mean(current[i,0]**2))
    rmsv = np.sqrt(np.mean(voltage[i,0]**2))
    Irms.append(rmsi)
    Vrms.append(rmsv)
    
Irms = np.array(Irms)
Vrms = np.array(Vrms)

S = Irms*Vrms

# current = vector containings current signals
# voltage = vector containings voltage signals
