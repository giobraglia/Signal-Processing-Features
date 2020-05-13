# Moving average filter
# the window_size parameter stands for the lenght of the interval over which the filtering
# will be performed

import pandas as pd
import numpy as np

def moving_average(signal,window_size):
    numbers_series = pd.Series(signal)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()

    moving_averages_list = moving_averages.tolist()
    without_nans = moving_averages_list[window_size - 1:]
    return without_nans
