# this type of extraction takes into account that all the signals are provided as audiofiles.flac
# voltage and current scale factors are employed to recover the real amplitude of all 840 measurements

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import soundfile as sf #special library to read and manipulate audio files
from glob import glob

#%%
def loadfiles(current_audiofiles,voltage_audiofiles,c_scalef,v_scalef):
    
    current = []
    voltage = []
    	
    for i in np.arange(len(current_audiofiles)):
        audio, freq = sf.read(current_audiofiles[i])
        current.append([audio])

    for i in np.arange(len(voltage_audiofiles)):
        audio, freq = sf.read(voltage_audiofiles[i])
        voltage.append([audio])
    
    current = np.array(current)
    voltage = np.array(voltage)
    
    # de-normalization with scale factor
        
    for i in np.arange(len(current_audiofiles)):
        current[i,0] *= c_scalef[i]
        voltage[i,0] *= v_scalef[i]	
    
    time = (np.arange(0,len(audio))/freq)
    

    return current,voltage,time,freq


#%%
#this function is used to change the sort from 'ASCIIBetical' to numeric by isolating the number in the filename

def keyFunc(afilename):
    nondigits = re.compile("\D")
    return int(nondigits.sub("", afilename))


#%%
#set directory for source files

data_dir1 = r"your\file\path\Current"
current_files = sorted(glob(data_dir1+'/*.flac'), key=keyFunc)

data_dir2 = r"your\file\path\Voltage"
voltage_files = sorted(glob(data_dir2+'/*.flac'), key=keyFunc)

df = pd.read_excel(r"path\to\scalefactors.xlsx")   # here scale factors where saved into a .xlsx file




#%%
c_scale = np.array(df.iloc[:,0],dtype='float32')      
v_scale = np.array(df.iloc[:,1],dtype='float32')

current, voltage, time, sampling_frequency = loadfiles(current_files,voltage_files,c_scale,v_scale)


