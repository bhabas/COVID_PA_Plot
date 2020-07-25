import gspread

# from oauth2client.service_account import ServiceAccountCredentials
# scope = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive',
#     'https://spreadsheets.google.com/feeds'
    
# ]
# creds = ServiceAccountCredentials.from_json_keyfile_name("gspread_creds.json", scope)
# client = gspread.authorize(creds)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1YI8zwQGTCmZS8t829LaHHGMETBE1bvCzHo87Yovll4U/edit#gid=550328143")
# ws_14day = sh.get_worksheet(4)
# dates = ws_14day.row_values(1)
# numbers = ws_14day.row_values(109)

def csv_to_array(): # converts csv to data array
    df = pd.read_csv("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - 14 Day per 100k by Region_County.csv", delimiter=',')
    df = df.replace(np.nan,0)
    df = df.replace(',','', regex=True)
    data_array = df.to_numpy()

    return(data_array)

def index_finder(data,location): # Returns index loc of county and created dict
    data_dict = {}
    for A, B in zip(data[:,0],data[:,1]):
        data_dict[A] = B

    index_loc = list(data_dict.keys()).index(location)

    return index_loc,data_dict

def biwk_avg_plot(dates,biwk_avg,location):
        fig = plt.figure()
        fig.tight_layout()

        ax = fig.add_subplot(111)
        ax = fig.gca()
        ax.grid()
        ax.plot(dates,biwk_avg)


        ax.axhline(y=50,c='0.55',linestyle='--',dashes = (10,5))
        ax.text(2,51,'50 Cases per 14 Days')
        # ax.set_ylim(0,100)
        ax.set_xlim(0)
        ax.set( ylabel= '14 Day per 100k', 
            xlabel = 'Date',
            title = '%s County' %(location))
        plt.show()



if __name__ == "__main__":

    location = "Allegheny"

    data_total = csv_to_array()
    sum_data =  data_total[0:83,:]
    region_avg = data_total[85:90,:]
    county_avg = data_total[94:160,:]


    dates = np.arange(0,data_total.shape[1]-2)



    index_loc =  index_finder(county_avg,location)[0]   
   

    biwk_avg = county_avg[index_loc,2:].astype(np.int)


    biwk_avg_plot(dates,biwk_avg,location)