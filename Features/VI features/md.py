# Maximum distance from the origin
# Displays the maximum distance from a point in the trajectory and the origin
# This feature comes from : 

import numpy as np

md=[]

for i in np.arange(len(c_cycle)):
    dist=[]
    for j in np.arange(len(c_cycle[i])):
        dist.append(np.linalg.norm([v_cycle[i][j],c_cycle[i][j]]))
    md.append(max(dist))
    
md=np.array(md)



# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# (see pick_cycle.py)
