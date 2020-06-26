# Length of the trajectory
# This feature comes from : MULINARI, B. M., CAMPOS, D. P., COSTA, C. H., ANCELMO, H. C., LAZZARETTI, A. E., OROSKI, E., LIMA, C. R. E., RENAUX, D. P. B., POTTKER, F.,
# LINHARES, R. R. "A New Set of Steady-State and Transient Features for Power Signature Analysis Based on V-I Trajectory".
# Accepted in: IEEE PES Innovative Smart Grid Technology Latin America, 2019.

import numpy as np

len_ = []

for i in np.arange(len(c_cycle)):
    lenght = 0
    for j in np.arange(len(c_cycle[i])-1):
        lenght += math.sqrt((c_cycle[i][j+1]-c_cycle[i][j])**2+(v_cycle[i][j+1]-v_cycle[i][j])**2)
        
    len_.append(lenght)
    
len_ = np.array(len_)


# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# (see pick_cycle.py ) 
