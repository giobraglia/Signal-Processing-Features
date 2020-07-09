# This is the function used create the current and voltage signal over which perform the features extraction .
# The reason why is called 'buffer' is because 20 cycles (settled with the parameter n_cycles) of the current signal, before
# the beginning of the transient, are buffered and then subtracted the part of the signal that has to be processed ('t' or 's') .
# The reason why this is done is to disaggregate a single appliance in a signal that might contain contributes from multiple appliances .
# In particular here, since I was dealing with the COOLL dataset, signals with a period of 2000 samples are considered. Moreover, for the
# steady-state it is sufficient to use just 20 cycles for features extraction.
#
# PARAMETERS :
# t_start, t_end = start and end instants of the transient ( calculated through Detector.py) ;
# c_signal, v_signal = respectively current and voltage signal ;
# part = if 't' perform disaggregation over the  transient, if 's' over the steady-state ;
# n_cycles = number of cycles that has to be buffered and lenght of the output steady-state signal


import numpy as np
import moving_average

def buffer (t_start,t_end,c_signal,v_signal, part, n_cycles = 20):   # part == 's' --> steady state
                                                                     # part == 't' --> transient state
    phi = t_start%2000 - t_end%2000
    temp_c = c_signal[t_start - (n_cycles+2)*2000 : t_start -2*2000] 
    
    if part == 's' :
        
        curr = c_signal[ t_end+phi +2*2000 : t_end+phi+(n_cycles+2)*2000  ] - temp_c
        volt = v_signal[ t_end+phi +2*2000 : t_end+phi+(n_cycles+2)*2000 ]  
 
    if part == 't' :

        diff = t_end - t_start
        curr = c_signal[ t_end+phi +2*2000 : t_end+phi+diff +2*2000  ] - temp_c[:diff]
        volt = v_signal[ t_end+phi +2*2000 : t_end+phi+diff +2*2000 ]                                                                 

    curr = np.array(moving_average(curr,4))
    volt = np.array(moving_average(volt,4))
    
    return curr,volt
    
    
# note that at the end the signal are smoothed through the moving_average filter in a way to obtain better features
# (see 
