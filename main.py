import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feeds'
    
]

creds = ServiceAccountCredentials.from_json_keyfile_name("gspread_creds.json", scope)

client = gspread.authorize(creds)




sh = client.open_by_url("https://docs.google.com/spreadsheets/d/1YI8zwQGTCmZS8t829LaHHGMETBE1bvCzHo87Yovll4U/edit#gid=550328143")

ws_14day = sh.get_worksheet(4)


dates = ws_14day.row_values(1)