# this type of extraction takes into account that all the signals are provided as audiofiles.flac
# voltage and current scale factors are employed to recover the real amplitude of all 840 measurements



def loadfiles(current_audiofiles,voltage_audiofiles,c_scalef,v_scalef):
    
    current=[]
    voltage=[]
    	
    for i in np.arange(len(current_audiofiles)): #np.arange(20):
        audio, freq = sf.read(current_audiofiles[i])
        current.append([audio])

    for i in np.arange(len(voltage_audiofiles)):
        audio, freq = sf.read(voltage_audiofiles[i])
        voltage.append([audio])
    
    current=np.array(current)
    voltage=np.array(voltage)
    
    #scale factor processing
        
    for i in np.arange(len(current_audiofiles)):
        current[i,0]*=c_scalef[i]
        voltage[i,0]*=v_scalef[i]	
    
    time=(np.arange(0,len(audio))/freq)
    

    return current,voltage,time,freq





#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import soundfile as sf #special library to read and manipulate audio files


#set directory for source files

data_dir1=r"path\of\file\Current"
current_files= glob(data_dir1+'/*.flac') # /* reads all the value with extention .flac

data_dir2=r"path\of\file\Voltage"
voltage_files= glob(data_dir2+'/*.flac')

df=pd.read_excel(r"path\to\scale_factors.xlsx")




#%%
#read audiofiles and create the time array
c_scale=np.array(df.iloc[:,0],dtype='float32')
v_scale=np.array(df.iloc[:,1],dtype='float32')

current,voltage,time, sampling_frequency=loadfiles(current_files,voltage_files,c_scale,v_scale)
