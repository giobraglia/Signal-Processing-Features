# Distance between maximum and minimum point
# This feature comes from : A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features 
# of V–I trajectory" Electric Power Systems Research, 2018.

import math
import numpy as np

dbp=[]

for i in np.arange(len(c_cycle)):
    m,M= np.argmin(c_cycle[i]), np.argmax(c_cycle[i])
    dbp.append(math.sqrt((c_cycle[i][M]-c_cycle[i][m])**2+(v_cycle[i][M]-v_cycle[i][m])**2))
    
dbp=np.array(dbp)


# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# (see pick_cycle.py)
