import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np

def plot_biwk_sum(data,locations,dates,pop_dict):
    ## Figure Initializing

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
        d_mvs = D.rolling(roll_amount).sum() # new cases in past [14] 
        d_mvs_pop = d_mvs/pop_factor # new cases in past [14] days per 100k

        wk_new_cases = int(np.sum(case_delta[-8:-1]))
        total_cases = int(np.sum(case_delta[:]))

        plt.plot(dates[2:],d_mvs_pop, label=locations[i] + ' County')
        plt.plot([],[],label = "Total Cases: " + f"{total_cases:,}", color = "white")
        plt.plot([],[],label = "Weekly New Cases: " + f"{wk_new_cases:,}" ,color = "white")
        

    ax.set( 
        ylabel= 'Cases', 
        xlabel = 'Date',
        title = 'Avg COVID-19 Cases in Last 14 Days per 100k People'
        )


    ax.legend(loc='upper center', ncol = len(locations), bbox_to_anchor=(0.5, -0.3))
    fig.subplots_adjust(bottom = 0.1)

    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.tight_layout()
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