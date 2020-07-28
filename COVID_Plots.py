import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np

def biwk_avg_plot(dates,biwk_avg,location):

        ## Initialize Figure and plot biwk data
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()
        ax.plot(dates,biwk_avg)


        ax.axhline(y=50,c='0.55',linestyle='--',dashes = (10,5))
        # ax.axvline(x = datetime.date(2020,5,25))
        # ax.axvline(x = datetime.date(2020,7,4))
        ax.text(2,51,'50 Cases per 14 Days')

       
        if np.max(biwk_avg) <= 100:
            ax.set_ylim(0,80)

        ax.set( 
            ylabel= '14 Day per 100k', 
            xlabel = 'Date',
            title = '%s County' %(location)
            )

        ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        plt.show()

def index_finder(data,location): # Returns index loc of county and created dict
    data_dict = {}
    for A, B in zip(data[:,0],data[:,1]):
        data_dict[A] = B

    index_loc = list(data_dict.keys()).index(location)

    return index_loc, data_dict

def biwk_mult_plot(dates,county_avg,locations):
        
    
    ## Initialize Figure and plot biwk data
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    index_loc = []
    for i in range(len(locations)):
        index_loc.append(index_finder(county_avg,locations[i]))
        # ax.plot(dates,county_avg[index_loc[i],2:])


    # ax.axhline(y=50,c='0.55',linestyle='--',dashes = (10,5))
    # # ax.axvline(x = datetime.date(2020,5,25))
    # # ax.axvline(x = datetime.date(2020,7,4))
    # # ax.text(2,51,'50 Cases per 14 Days')


    # # if np.max(biwk_avg) <= 100:
    # #     ax.set_ylim(0,80)

    # ax.set( 
    #     ylabel= '14 Day per 100k', 
    #     xlabel = 'Date',
    #     # title = '%s County' %(location)
    #     )

    # ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=(1,15)))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    # plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
    plt.show()

    return index_loc