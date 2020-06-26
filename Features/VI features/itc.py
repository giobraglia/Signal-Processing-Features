# Current span is simply calculated as itc = Imax - Imin

# This feature comes from : A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features 
# of V–I trajectory" Electric Power Systems Research, 2018.

import numpy as np

#%%
# itc calculated over a sigle period

span = []

for i in np.arange(len(current)):
    span.append(np.max(c_cycle[i])-np.min(c_cycle[i]))
    
span = np.array(span)

#%%
# itc calculated over a signal containing multiple periods (to increase the robustness of the feature)

span = []

for i in np.arange(len(current)):
  peakM , _ = find_peaks(current_cycle[i],distance=1400)    # here distance 1400 was settled empirically
  peakm , _ = find_peaks(-current_cycle[i],distance=1400)
  span.append(np.mean(current_cycle[i][peakM])-np.mean(current_cycle[i][peakm]))
    
span = np.array(span)

# current : vector containings current signals
# current_cycle : vector containings small portions of the signals analysed in steady-state
# c_cycle : vector whose elements are periods of the current signals analysed
# (see pick_cycle.py)


















