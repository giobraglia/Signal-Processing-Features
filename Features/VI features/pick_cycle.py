# The next code can be used to pick a cycle (a period) of the signal inside the steady-state.
# Since VI trajectories will be analyzed, it's important to pick voltage and current cycles belonging to the same istants
# in the signal. Here the voltage signal will be used as a reference for both. In particular the cycle is taken by detecting
# a part of the steady-state signal among two peaks of the voltage.
#
# The algorithm goes through the following steps:
#               1- isolate a part of steady-state signal ;
#               2- smoothing noise with a simple moving-average filter (see moving_average.py);
#               3- isolate one cycle in the latter .

import numpy as np
from scipy.signal import find_peaks

#%%
#STEP 1 & 2

current_cycle = []
voltage_cycle = []

for i in np.arange(len(current)):
   current_cycle.append(moving_average(current[i,0][300000:309000],140)) 
   voltage_cycle.append(moving_average(voltage[i,0][300000:309000],140))

   
current_cycle = np.array(current_cycle)
voltage_cycle = np.array(voltage_cycle)

#%%
#STEP 3 

c_cycle = []
v_cycle = []

for i in np.arange(len(current_cycle)):
  max_, _ = find_peaks(voltage_cycle[i],distance=1400)
  c_cycle.append(current_cycle[i,max_[1]:max_[2]])
  v_cycle.append(voltage_cycle[i,max_[1]:max_[2]])

c_cycle = np.array(c_cycle)
v_cycle = np.array(v_cycle)


# all the numeric data inserted into the algorithm are given as an example ; in particular (as you can see in
# STEP 1 & 2) knowing the nature of the signals from the specifics of COOLL dataset, it can be possible to spot
# a steady-state portion of the signal among indeces 300000:309000
