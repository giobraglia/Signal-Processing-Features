# Angle between maximum and minimum points
# This feature comes from : MULINARI, B. M., CAMPOS, D. P., COSTA, C. H., ANCELMO, H. C., LAZZARETTI, A. E., OROSKI, E., LIMA, C. R. E., RENAUX, D. P. B., POTTKER, F.,
# LINHARES, R. R. "A New Set of Steady-State and Transient Features for Power Signature Analysis Based on V-I Trajectory".
# Accepted in: IEEE PES Innovative Smart Grid Technology Latin America, 2019.

import numpy as np

angp = []

for i in np.arange(len(c_cycle)):
    m, M = np.argmin(c_cycle[i]), np.argmax(c_cycle[i]) 
    slope = (c_cycle[i][M]-c_cycle[i][m])/(v_cycle[i][M]-v_cycle[i][m])
    angp.append(np.arctan(slope))
    
angp = np.array(angp)

# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# (see pick_cycle.py)
