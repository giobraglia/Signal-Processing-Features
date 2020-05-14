# Calculates the peak of the power signal

import numpy as np

peak = []
for i in np.arange(len(power)):
    peak.append(np.max(power[i,:]))

peak = np.array(peak)

# power : vector containings power signals
