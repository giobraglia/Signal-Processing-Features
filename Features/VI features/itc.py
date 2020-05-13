# Current span is simply calculated as itc = Imax - Imin

import numpy as np

span=[]

for i in np.arange(len(current)):
    span.append(np.max(current_cycle[i])-np.min(current_cycle[i]))
    
span=np.array(span)






















