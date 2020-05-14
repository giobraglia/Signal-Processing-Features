# Computes the mean value of the derivative of the transient, from its peak to
# its end ( beginning of the steady-state).
#
# First step back to envelope.py to understand how power_der and obtained .


import numpy as np

mean_slope = []

for i in np.arange(len(power_der)):
    mean_slope.append(np.mean(power_der[i][0:index_steady_begin[i]]))  # power_der signals already start from the peak
                                                                       # of the transient, thus the latter has not
                                                                       # to be computed
mean_slope = np.array(mean_slope)
