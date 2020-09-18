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
    population = df.loc[(df['STNAME'] == state) & (df['CTYNAME'] == county+" County")].values[0,18]
    return(population)

def state_pop_lookup(state):
    df = pd.read_csv('co-est2019-alldata.csv', encoding = "latin")
    population = df.loc[(df['STNAME'] == state) & (df['CTYNAME'] == state)].values[0,18]
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


def plot_state_data(state):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
    df = pd.read_csv(url, delimiter=',')

    ## Dates Initialization
    start_index = df.columns.get_loc("3/15/20") # Specified start date of data
    dates = list(df.columns.values[start_index:])
    dates = [datetime.strptime(x, '%m/%d/%y') for x in dates]
    today = datetime.today().strftime('%m/%d/%y')


    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.grid()

    for i in range(len(state)):
        population = state_pop_lookup(state[i])
        pop_factor = population/100e3 # per 100k people

        group = df.loc[(df['Province_State'] == state[i])].values[:,64:]
        case_delta = np.diff(group, prepend=0)
        case_delta = np.sum(case_delta,axis=0)

        D = pd.Series(case_delta)
        d_mvs = D.rolling(7).sum()/pop_factor # new cases in past [14]


        wk_new_cases = int(np.sum(case_delta[-8:]))
        total_cases = int(np.sum(case_delta[:]))

        plt.plot(dates,d_mvs, label=state[i])
        plt.plot([],[],label = "Total Cases: " + f"{total_cases:,}", color = "white")
        plt.plot(dates[-8:],d_mvs[-8:],linewidth = 5, alpha = 0.6, color = "gray")
        plt.plot([],[],label = "Cases in Past Week: " + f"{wk_new_cases:,}",color = "white")
        plt.plot([],[],label = "Population: "+ f"{population:,}",color = "white")

    ax.set(
        ylabel= 'Cases',
        xlabel= 'Date',
        title= 'COVID-19 | Daily Cases per 100k People ({})'.format(today)
        )


    plt.ylim(0)

    ax.legend(ncol = len(state), loc='upper center', bbox_to_anchor=(0.5, -0.5))
    fig.subplots_adjust(bottom = 0.1)

    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

    plt.tight_layout()
    plt.show()

    fig.savefig(state[0] + "daily_cases.png")


