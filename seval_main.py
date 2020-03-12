from SEVAL.Clustering import seval_funcs
from SEVAL.g_sheets import gs_funcs
from oauth2client.service_account import ServiceAccountCredentials
import gspread
###
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/david/PycharmProjects/SEVAL/Creds/seval-270420-f0725c9a2188.json", scope)
client = gspread.authorize(creds)

CORPUS_PATH = '/Users/david/PycharmProjects/LSTM-Text-Generator/MainModules/MainPackage/HP5.txt'

# Find a workbook by name and open the first sheet
sheet = client.open("AutoSentenceEval").sheet1

# convert raw text into documents
documents = seval_funcs.text_2_list(CORPUS_PATH)

# initialise g_sheet row
row = 90

#for i in range(len(sheet.col_values(1))):
for i in range(3):
    # Get values from g_sheet
    word_count = gs_funcs.get_word_count(row)
    sentence = gs_funcs.get_sentences(row)

    # update values in g_sheet
    words_in_clus = seval_funcs.cluster_texts(documents, sentence, word_count, 250)[0]
    entropy = seval_funcs.cluster_texts(documents, sentence, word_count, 250)[1]
    gs_funcs.update_metrics(row, words_in_clus, entropy)

    row += 1

