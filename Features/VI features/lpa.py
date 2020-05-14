# Area with loop direction
#
# This feature is an implementation of the formula for lpa contained in the paper:
# A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features 
# of V–I trajectory" Electric Power Systems Research, 2018.

import numpy as np

lpa=[]

for i in np.arange(len(current_cycle)):
    lpa.append(np.sum(0.5*(v_cycle[i][1:-1]-v_cycle[i][0:-2])*(c_cycle[i][1:-1]-c_cycle[i][0:-2])))

lpa=np.array(lpa)

# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# current_cycle = vector containings small portions of the signals analysed in steady-state
# (see pick_cycle.py)
