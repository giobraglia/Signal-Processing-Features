# This function allows to find turn-on (ts) and turn-off (te) instant of appliances when we are working over a signal
# containings multiple contributes from different appliances. This task will be accomplished by taking into account
# the envelope of the signal that we want to analyze and its variance.
# This is the implementation in python of the algorithm proposed in the paper :
#
#        M. Nait Meziane, P. Ravier, G. Lamarque, J. Le Bunetel and Y. Raingeaud, 
#        "High accuracy event detection for Non-Intrusive Load Monitoring," 2017 IEEE International Conference on Acoustics, 
#        Speech and Signal Processing (ICASSP), New Orleans, LA, 2017, pp. 2452-2456, doi: 10.1109/ICASSP.2017.7952597.
#        
# In particular the formula used to compute the standard variance is a little bit changed since, in python, the formula#
# proposed always bring to an overflow of the values.
# (for the used formula see https://people.revoledu.com/kardi/tutorial/RecursiveStatistic/Time-Variance.htm )
# The function takes as input : 
#           - signal = numpy array
#           - window = number of samples over which the variance will be iteratively calculated
#           - threshold = empirically settled value to detect ts and te
# Returns :
#           - ts = vector containings the start instants of the appliances (start of the transient)
#           - te = vector containings the end instants of the appliances
#           
# In particular, in this code the function moving_average() will be exploited to smooth the signal 
# (see Signal-Processing-Features/Features/VI features/moving_average.py ) 
#

import numpy as np
from scipy.signal import find_peaks


def detector(signal, window, threshold):
    
    temp = 0
    ts = []  # turn-on instants
    te = []  # turn-off instants
    
    #create envelope of signal
    peak , _ = find_peaks(np.abs(signal),distance=2000)           # distance = 2000 was taken because each signal
    env = moving_average(np.abs(signal[peak]),2)                  # analysed had a period of 2000 samples
    env = np.array(env)
    
    
    signal_std = np.zeros(len(env))
    signal_mean = np.zeros(len(env))
    
    #initialize variance and mean vector
    signal_std[0:window] = np.std(env[0:window])
    signal_mean[0:window] = np.mean(env[0:window])
    
    for i in np.arange(window, len(env)-window , window ):
        for j in np.arange(0,window):
            signal_mean[i+j] = signal_mean[i+j-1] + (env[i+j]-env[i+j-window])/window  
            signal_std[i+j] = np.sqrt((window-1)/window * signal_std[i+j-1]**2 + 1/(window-1) * (env[i+j]-signal_mean[i+j])**2 )

    
    std_grad = np.gradient(signal_std) 
    env_grad = np.gradient(env)
    
    
    #find ts and te instants
    for i in np.arange(0,len(env)):
        
        if ( signal_std[i] > threshold and std_grad[i] > 0 and env_grad[i] > 0 and temp == 0 ) : 
            temp = 1
            ts.append([i,peak[i]])
            
        if ( signal_std[i] < threshold and std_grad[i] < 0 and temp == 1 ) :            
            te.append([i,peak[i]])           
            temp = 0
            
    # i = index of the event on the envelope signal
    # peak[i] = index of the event in the original signal

    
    ts = np.array(ts)
    te = np.array(te)
    
    return ts,te 
