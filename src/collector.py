import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

email = os.getenv('USAJOBS_EMAIL')
key_url = os.getenv('USAJOBS_API_KEY')

headers = {
    'Host': 'data.usajobs.gov',
    'User-Agent': email,
    'Authorization-key': key_url
}

r = requests.get("https://data.usajobs.gov/api/search", headers=headers)

print(r.status_code)

with open('/Users/amadoubarrie/Desktop/job-market-pipeline/data/raw/raw_jobs.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(),f, ensure_ascii=False, indent= 4)