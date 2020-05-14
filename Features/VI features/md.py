# Maximum distance from the origin
# Displays the maximum distance from a point in the trajectory and the origin
# This feature comes from : MULINARI, B. M., CAMPOS, D. P., COSTA, C. H., ANCELMO, H. C., LAZZARETTI, A. E., OROSKI, E., LIMA, C. R. E., RENAUX, D. P. B., POTTKER, F.,
# LINHARES, R. R. "A New Set of Steady-State and Transient Features for Power Signature Analysis Based on V-I Trajectory".
# Accepted in: IEEE PES Innovative Smart Grid Technology Latin America, 2019.

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
