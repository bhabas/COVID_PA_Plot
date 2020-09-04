import pandas as pd
import numpy as np
from datetime import datetime
import pkg.Covid_Plots as cp

import matplotlib.pyplot as plt
import matplotlib.dates as mdates




def csv_to_array(file): # converts csv to data array
    df = pd.read_csv(file, delimiter=',')
    data_array = df.to_numpy()

    return(data_array, df)


df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")


dates = df.columns.values.tolist()[64:]


## Data Import

# County Data


# locations = np.array([["Erie", "PA"], ["Centre", "PA"]])






# cp.plot_biwk_sum(locations)

























# for j in range(0,2):
#     if j == 0:
#         locations = ["Erie","Centre"]
#     elif j==1:
#         locations = ["Allegheny","Philadelphia"]
#     else:
#         pass

#     cp.plot_biwk_sum(county_data,locations,dates,pop_dict)
        


# cp.plot_state_data(state_data, dates)


