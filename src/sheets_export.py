import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe


data = pd.read_csv('/Users/amadoubarrie/Desktop/job-market-pipeline/data/cleaned/cleaned_jobs.csv')

gc = gspread.service_account(filename='google-credentials.json')
sh = gc.open("hirehunt jobs")
worksheet = sh.sheet1
set_with_dataframe(worksheet, data)
print(worksheet.get('B2'))