import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pkg.Covid_Plots as cp



## Data Import

# County Data
# Penn State, Ohio State, Univ. of Florida, Liberty Univ., Texas A&M, Illinois at Urbana-Champaign 

locations = np.array([
["Centre", "PA", "Pennsylvania"], # Penn State
["Los Angeles", "CA", "California"],
["New York", "NY", "New York"]])

locations = np.array([
["Erie", "PA", "Pennsylvania"], # Penn State
["Summit", "OH", "Ohio"],
["Mecklenburg", "NC", "North Carolina"]])



cp.plot_biwk_sum(locations)




state = ["Pennsylvania","North Carolina","Ohio"]
cp.plot_state_data(state)

