import pandas as pd
import numpy as np
import datetime
import pkg.Covid_Plots as cp

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def csv_to_array(file): # converts csv to data array
    df = pd.read_csv(file, delimiter=',')
    df = df.replace(np.nan,0)
    df = df.replace(',','', regex=True)
    data_array = df.to_numpy()

    return(data_array)

# if __name__ == "__main__":



## Data Import
state_data = csv_to_array("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - Pgh MSA Data.csv")
county_data = csv_to_array("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - 14 Day per 100k by Region_County.csv")

county_avg = county_data[94:160,:]

## County Population Dictionary
pop_dict = {}
for A, B in zip(county_avg[:,0],county_avg[:,1]):
    pop_dict[A] = B

## Date Initialization
dates = list(range(0,county_data.shape[1]))
start_date = datetime.date(2020, 3, 8)
for i in dates:
    dates[int(i)] = start_date + datetime.timedelta(days=int(i))

for j in range(0,2):
    if j == 0:
        locations = ["Erie","Centre"]
    elif j==1:
        locations = ["Allegheny","Philadelphia"]
    else:
        pass

    cp.plot_biwk_sum(county_data,locations,dates,pop_dict)
        


cp.plot_state_data(state_data, dates)


