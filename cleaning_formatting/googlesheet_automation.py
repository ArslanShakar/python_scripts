import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# client = gspread.authorize(credentials=creds)
# sheet = client.open("unclean_sheet").sheet1

gs = gspread.service_account(filename='credentials.json')
sheet = gs.open("unclean_sheet").sheet1
rows = sheet.get_all_records()

print(rows)
