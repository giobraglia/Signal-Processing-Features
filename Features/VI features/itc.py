# Current span is simply calculated as itc = Imax - Imin

# This feature comes from : A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features 
# of V–I trajectory" Electric Power Systems Research, 2018.

import numpy as np

span=[]

for i in np.arange(len(current)):
    span.append(np.max(current_cycle[i])-np.min(current_cycle[i]))
    
span=np.array(span)


# current = vector containings current signals
# current_cycle = vector containings small portions of the signals analysed in steady-state
# (see pick_cycle.py)


















