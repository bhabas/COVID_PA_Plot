import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import numpy as np

from datetime import datetime
# data = county_data

def plot_biwk_sum(data,locations,dates,pop_dict):
    today = datetime.today().strftime('%m/%d/%y')

    county_sum =  data[0:83,:]

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
        case_delta[138] = 4
        case_delta[142] = 0

        D = pd.Series(case_delta)
        d_mvs = D.rolling(roll_amount).sum() # new cases in past [14] 
        d_mvs_pop = d_mvs/pop_factor # new cases in past [14] days per 100k

        wk_new_cases = int(np.sum(case_delta[-8:]))
        total_cases = int(np.sum(case_delta[:]))

        plt.plot(dates[2:],d_mvs_pop, label=locations[i] + ' County')
        plt.plot([],[],label = "Total Cases: " + f"{total_cases:,}", color = "white")
        plt.plot(dates[-8:],d_mvs_pop[-8:],linewidth = 5, alpha = 0.6, color = "gray")
        plt.plot([],[],label = "Cases in Past Week: " + f"{wk_new_cases:,}",color = "white")
        


    ax.set( 
        ylabel= 'Cases', 
        xlabel = 'Date',
        title = 'COVID-19 | 14 Day sum per 100k People ({})'.format(today)
        )


    ax.legend(loc='upper center', ncol = len(locations), bbox_to_anchor=(0.5, -0.3))
    fig.subplots_adjust(bottom = 0.1)

    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.tight_layout()
    plt.show()
    
    fig.savefig(locations[0] + '_biwk_sum.png')


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

def plot_state_data(state_data, dates):



    today = datetime.today().strftime('%m/%d/%y')

    state_case_delta = state_data[9,1:].astype(int) # New cases per day
    roll_amount = 7
    D = pd.Series(state_case_delta)
    state_delta_mva = D.rolling(roll_amount).mean() # Creates a [7] day rolling average
    wk_cases_state = sum(state_case_delta[-7:])

    roll_amount = 5
    pos_rate = state_data[21,1:].astype('str') # Converts to string to remove % then back to float
    pos_rate = np.char.strip(pos_rate,"%")
    pos_rate = pos_rate.astype('float64')
    D = pd.Series(pos_rate)
    pos_rate_mva = D.rolling(roll_amount).mean() # [5] day rolling average
    wkavg_pos = int(np.average(pos_rate[-8:]))
    fig = plt.figure()

    ## ax1 Creation and Plotting
    ax1 = fig.add_subplot(111)
    ax1.grid()


    l1 = ax1.plot(dates[1:],state_delta_mva,label = "Daily PA Cases")
    ax1.plot(dates[-7:],state_delta_mva[-7:],linewidth = 5, alpha = 0.6, color = "gray")

    l2 = ax1.plot([],[],color = 'white', label = "Cases in past week: {:,}".format(wk_cases_state))
    ax1.set_ylim(bottom = 0)



    ax1.set( 
        ylabel= 'Cases', 
        title = 'PA New COVID-19 Cases per Day ({})'.format(today)
        )


    ## ax2 Creation and Plotting
    ax2 = ax1.twinx()
    l3 = ax2.plot(dates[1:],pos_rate_mva, color = "Orange", label = "Test Positivity Rate")
    l4 = ax2.plot([],[],color = "white", label = "7-Day Positivity Avg: {:.1f} %".format(wkavg_pos))
    ax2.plot(dates[-7:],pos_rate_mva[-7:],linewidth = 5, alpha = 0.6, color = "gray")
    ax2.set_ylabel('Test Positivity Rate (<10% is Good)')



    import matplotlib.ticker as mtick
    ax2.yaxis.set_ticks([0,10,20,40,60,80,100])
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax2.set_ylim(0, 100)


    ax1.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')



    leg = l1 + l2 + l3 + l4
    labs = [l.get_label() for l in leg]
    ax1.legend(leg, labs, loc = "upper right")


    plt.tight_layout()
    plt.show()

    fig.savefig('State_Data_fig.png')