import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import numpy as np

from datetime import datetime
# data = county_data

def fips_lookup(county,state):

    df = pd.read_csv('fips_dict.csv')
    fips = df.loc[(df['state'] == state) & (df['name'] == county + " County")].values[0,0]

    return(fips)

def pop_lookup(county,state):
    df = pd.read_csv('co-est2019-alldata.csv', encoding = "latin")
    population = df.loc[(df['STNAME'] == state) & (df['CTYNAME'] == county+" County")].values[0,7]
    return(population)


def plot_biwk_sum(locations):

    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
    df = pd.read_csv(url, delimiter=',')
    start_index = df.columns.get_loc("3/15/20") # Specified start date of data
    dates = list(df.columns.values[start_index:])
    dates = [datetime.strptime(x, '%m/%d/%y') for x in dates]

    today = datetime.today().strftime('%m/%d/%y')

    ## Figure Initializing

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.grid()

    for i in range(locations.shape[0]):
        fips = fips_lookup(locations[i,0], locations[i,1])
        case_data = df.loc[df['FIPS'] == fips].values[0,start_index:]


        ## Data Plotting
        population = pop_lookup(locations[i,0],locations[i,2])
        pop_factor = population/100e3 # per 100k people
        case_delta = np.diff(case_data, prepend=0)


        D = pd.Series(case_delta)
        d_mvs = D.rolling(14).sum() # new cases in past [14]
        d_mvs_pop = d_mvs/pop_factor # new cases in past [14] days per 100k

        wk_new_cases = int(np.sum(case_delta[-8:]))
        total_cases = int(np.sum(case_delta[:]))

        plt.plot(dates,d_mvs_pop, label=locations[i,0] + ' County, ' + locations[i,1])
        plt.plot([],[],label = "Total Cases: " + f"{total_cases:,}", color = "white")
        plt.plot(dates[-8:],d_mvs_pop[-8:],linewidth = 5, alpha = 0.6, color = "gray")
        plt.plot([],[],label = "Cases in Past Week: " + f"{wk_new_cases:,}",color = "white")
        plt.plot([],[],label = "Population: "+ f"{population:,}",color = "white")


    ax.set(
        ylabel= 'Cases',
        xlabel= 'Date',
        title= 'COVID-19 | 14 Day Sum per 100k People ({})'.format(today)
        )

    plt.ylim(0)

    ax.legend(ncol = 3, loc='upper center', bbox_to_anchor=(0.5, -0.5))
    fig.subplots_adjust(bottom = 0.1)

    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.tight_layout()
    plt.show()

    fig.savefig(locations[0,0] + "_biwk_sum.png")


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