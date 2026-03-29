import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import os
from google.api_core.exceptions import GoogleAPIError
import pyarrow



credentials = service_account.Credentials.from_service_account_file(
    "google-credentials.json"
    )

client = bigquery.Client(
    credentials = credentials,
    project="hirehunt-491215"
 )

df = pd.read_csv("cleaned_jobs.csv")

table_ref = "hirehunt-491215.job_market.cleaned_jobs"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)
job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

job.result()

table =client.get_table(table_ref)
print(f"loaded {table.num_rows} rows into {table_ref}")
