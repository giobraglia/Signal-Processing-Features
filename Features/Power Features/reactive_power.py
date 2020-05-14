# Calculates the reactive power of a power signal
# For the computation of the root mean square vectors Irms and Vrsm (relative to current and voltage)
# just step back to apparent_power.py
#
# This feature is calculated by simply exploiting the trigonometry relation that link the active, reactive and
# apparent power, i.e. Q = S * sin (theta) , theta = angle between P and Q.

import numpy as np

theta = np.arccos(P/S)
Q= S * np.sin(theta)

# P : active power vector (see active_power.py)
# S : apparent power vector (see apparent_power.py)
