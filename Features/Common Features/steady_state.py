# Computes the average steady-state value of a signal
# Since I've dealt with ac signals, to calculate this features the following steps were taken :
#       1 - calculate the envelope of the signal ; 
#       2 - compute the derivative of the envelope to find the beginning of the steady-state ( here calculated as
#           the end of the transient) and its end ( here simply the end of the signal) ;
#       3 - calculate the average value of the signal inside the steady-state .
#
# First step back to envelope.py to understand how point 1 and 2 are computed
# and how power_p_env, index_steady_begin, index_steady_end are obtained .

import numpy as np

steady_state = []

for i in np.arange(len(index_steady_begin)):
    mean_env = np.mean(power_p_env[i][index_steady_begin[i]:index_steady_begin[i]:index_steady_end[i]])
    steady_state.append(mean_env)
    
steady_state = np.array(steady_state)

