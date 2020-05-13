# Features
## Signals

All the signals are taken from the COOLL dataset and converted into a numpy array in Python to be processed (see the file
signal_extraction.py to understand how).
COOLL dataset display 840 measurements of 42 appliances, where for each of them 20 measurements were performed. At the end
of each algorithm, it could be useful to plot the respective feature : for good classification performaces a staircase-like
graph is preferred.

## Algorithms

All the algorithm presented are really simple and intuitive. At the end the algorithm will be always inserted into 'for'
cycle in order to span all the data and then getting the resulting feature.
'for' cycle are always very computationally expensive and low, usually vectorial operation in Python are preferred since
they are really optimize. Therefore if someone as some suggestions to optimize my calculus, please contact me.

