# Area of the VI trajectories.
# This feature is computed using the Shoelace's formula, used to calculate the area of 
# polygons, implemented in the file shoelace.py .
# It's important to say that Shoelace's formula doesn't work for polygons with a self-intercepting shape.
# By the way, the approximation given by this formula turned out to be useful, even for self-intercepting
# signals.

# This feature come from : 
# A. L. Wang, B. X. Chen, C. G. Wang, and D. D. Hua, "Non-intrusive load monitoring algorithm based on features 
# of V–I trajectory" Electric Power Systems Research, 2018.

import numpy as np

area_ = []

for i in np.arange(len(c_cycle)):
    area_.append(polygonArea(v_cycle[i], c_cycle[i],len(c_cycle[i])))
    
area_ = np.array(area_)


# c_cycle : vector whose elements are periods of the current signals analysed
# v_cycle : vector whose elements are periods of the voltage signals analysed
# (see pick_cycle.py)
