import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np

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


def plot_cum_cases(data,locations,dates):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ## Data Plotting
    for i in range(len(locations)):
        index_loc = list(data[:,0]).index(locations[i]) # finds index of a given county
        ax.plot(dates[2:],data[index_loc,2:])

    ax.set( 
        ylabel= 'Cases', 
        xlabel = 'Date',
        title = 'Cumulative Total of Cases'
        # legend: title = '%s County' %(locations[i])
        )
    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.show()

def plot_