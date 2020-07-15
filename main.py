import gspread

from oauth2client.service_account import ServiceAccountCredentials
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feeds'
    
]
creds = ServiceAccountCredentials.from_json_keyfile_name("gspread_creds.json", scope)
client = gspread.authorize(creds)



























import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1YI8zwQGTCmZS8t829LaHHGMETBE1bvCzHo87Yovll4U/edit#gid=550328143")
#ws_14day = sh.get_worksheet(4)
#dates = ws_14day.row_values(1)
#numbers = ws_14day.row_values(109)

df = pd.read_csv("/home/bhabas/Documents/Covid_Plot/COVID-19 Tracking Workbook - PA - 14 Day per 100k by Region_County.csv")
print(df.head(0))


def main():
    pass

if __name__ == "__main__":
    main()