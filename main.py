import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pkg.Covid_Plots as cp



## Data Import

# County Data


locations = np.array([
["Centre", "PA", "Pennsylvania"],
["Los Angeles", "CA", "California"],
["New York", "NY", "New York"]])

cp.plot_biwk_sum(locations)




state = ["Pennsylvania"]
cp.plot_state_data(state)

