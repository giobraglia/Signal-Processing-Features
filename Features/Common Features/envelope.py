# Computes the envelope of a signal .
# The envelope, for analysis purposes, will be just calculated from the peak value of the signal 
# (which usually stays in the transient) until its end .


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#%%

power_p_env = []
power_der = []

for i in np.arange(len(power)):
    j = np.argmax(power[i,:])              
    a = power[i,j:-1]
    peak , _ = find_peaks(a,distance=2000)  # Here 'distance=2000' has been choosen since this number correspond
                                            # to the period (in number of samples) of the signals
    power_p_env.append(a[peak])
    power_der.append(np.gradient(a[peak]))
    
power_p_env = np.array(power_p_env)      # array containings the envelope of the power signals
power_der = np.array(power_der)          # array containings the derivative of the power envelopes


#%%
# check algorithm by plotting (here as an example the 204th power signal is used )
# upper graph = envelope
# lower graph = envelope's derivative


i = np.argmax(power[204,:])
a = power[204,i:-1]
peak , _ = find_peaks(a,distance=2000)

plt.subplot(2,1,1)
plt.plot(a)
plt.plot(peak,a[peak],marker='x')
plt.grid() 

plt.subplot(2,1,2)
plt.plot(np.gradient(a[peak]),color='red')
plt.grid()

plt.show()


#%%
# Extrapolation of the instants relatives to the beginning and the end of the steady-state

index_steady_begin=[]
index_steady_end=[]

for i in np.arange(len(power_der)):
     c=0
     b=0
     for j in np.arange(len(power_der[i])):
        if power_der[i][j]>0 and c==0: 
            c=j
        if power_der[i][j]<-20:              # here the value -20 , for the detection of 
            b=j                              # the end of the steady-state, has been choosen empirically
            
            
     index_steady_begin.append(c)                                    
     index_steady_end.append(b)
     


index_steady_begin = np.array(index_steady_begin)
index_steady_end = np.array(index_steady_end)


# power : vector containings power signals



