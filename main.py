import pandas as pd
import numpy as np
import datetime
import COVID_Plots as cp

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def csv_to_array(file): # converts csv to data array
    df = pd.read_csv(file, delimiter=',')
    df = df.replace(np.nan,0)
    df = df.replace(',','', regex=True)
    data_array = df.to_numpy()

    return(data_array)

def index_finder(data,location): # Returns index loc of a given county and the created dict
    data_dict = {}
    for A, B in zip(data[:,0],data[:,1]):
        data_dict[A] = B

    index_loc = list(data_dict.keys()).index(location)

    return index_loc

# if __name__ == "__main__":



## Data Import
state_data = csv_to_array("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - Pgh MSA Data.csv")
county_data = csv_to_array("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - 14 Day per 100k by Region_County.csv")
county_sum =  county_data[0:83,:]
county_avg = county_data[94:160,:]

## County Population Dictionary
pop_dict = {}
for A, B in zip(county_avg[:,0],county_avg[:,1]):
    pop_dict[A] = B

## Date Initialization
dates = list(range(0,county_data.shape[1]))
# dates = list(range(0,7))
start_date = datetime.date(2020, 3, 8)
for i in dates:
    dates[int(i)] = start_date + datetime.timedelta(days=int(i))


locations = ["Erie","Centre"]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()


for i in range(len(locations)):
    index_loc = list(county_sum[:,0]).index(locations[i]) # finds index of a given county
    ax.plot(dates[2:],county_sum[index_loc,2:])

plt.show()

