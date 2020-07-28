import pandas as pd
import numpy as np
import datetime
# import COVID_Plots as cp

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


# cp.plot_cum_cases(county_sum,locations,dates)

# cp.biwk_avg_plot(county_sum,locations,dates,pop_dict)


def plot_biwk_sum(data,locations,dates,pop_dict):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ## Data Plotting
    for i in range(len(locations)):
        roll_amount = 14
    
        pop_factor = int(pop_dict[locations[i]])/100e3 # per 100k people


        index_loc = list(data[:,0]).index(locations[i]) # finds index of a given county
        case_delta = np.diff(data[index_loc,2:],prepend=0)

        D = pd.Series(case_delta)
        d_mva = D.rolling(roll_amount).sum()/pop_factor # new cases in past [14] days per 100k

        plt.plot(dates[2:],d_mva)

    ax.set( 
        ylabel= 'Cases', 
        xlabel = 'Date',
        title = '14 Day Case Increase per 100k People'
        # legend: title = '%s County' %(locations[i])
        )
    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.show()


plot_biwk_sum(county_sum,locations,dates,pop_dict)

