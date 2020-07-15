import gspread


from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feeds'
    
]

creds = ServiceAccountCredentials.from_json_keyfile_name("gspread_creds.json", scope)
client = gspread.authorize(creds)