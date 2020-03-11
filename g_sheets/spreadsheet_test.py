
from collections import Counter
import textstat
import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/david/PycharmProjects/SEVAL/Creds/seval-270420-f0725c9a2188.json", scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("AutoSentenceEval").sheet1

# TODO : Make function for each column of SEVAL

# Calculate & generate sentence word count
row = 2
sheet.insert_row(["WbasedModel2", " "], row)

#Calculate sentence Flesch Reading Ease


#textstat.gunning_fog(text)
#textstat.smog_index()