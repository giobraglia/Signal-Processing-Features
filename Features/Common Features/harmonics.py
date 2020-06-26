# Computes the amplitude of the armonics of the signal.
# All the signals analysed from the COOLL dataset referred to appliances undergoing
# a supply power at 50 Hz, therefore I founded empirically that the most relevant harmonics
# was from 0 to 2400 Hz with a step of 200 Hz and this is because I'm going to calculate FFT over
# a signal made of 200000 samples ( with a signal of 140000 samples I would find relevant components 
# by using a step of 140 Hz for example) .

import numpy as np

harmonics = np.zeros([840,12])
a = np.arange(0,2400,200)

for i in np.arange(len(power)):
    fft = np.fft.fft(power[i,200000:400000])
    fp = np.abs(fft)/len(power[i,200000:400000])*2
    for ind,j in enumerate(a):
        if j==0:
            harmonics[i,ind] = fp[j] 
        else:
            harmonics[i,ind] = np.max(fp[j-10:j+10])  
            
# power : vector containings power signals          
