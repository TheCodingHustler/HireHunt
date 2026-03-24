import json
import pandas as pd


with open('/Users/amadoubarrie/Desktop/job-market-pipeline/data/raw/raw_jobs.json','r') as file:
    data = json.load(file)
    jobs=[]
    for job in data["SearchResult"]["SearchResultItems"]:
      dataList = {
                  "job-title": job["MatchedObjectDescriptor"]["PositionTitle"], 
                  "Location":  job["MatchedObjectDescriptor"]["PositionLocation"][0]["LocationName"],
                  "Organization": job["MatchedObjectDescriptor"]["OrganizationName"], 
                  "min-salary": job["MatchedObjectDescriptor"]["PositionRemuneration"][0]["MinimumRange"],
                  "max-salary": job["MatchedObjectDescriptor"]["PositionRemuneration"][0]["MaximumRange"],
                  "RateInterval": job["MatchedObjectDescriptor"]["PositionRemuneration"][0]["RateIntervalCode"]
                  }
      jobs.append(dataList)
    df = pd.DataFrame(jobs)
    cols = ['min-salary', 'max-salary']
    df[cols] = df[cols].apply(pd.to_numeric, errors = 'coerce')
    df.loc[df["RateInterval"] == "PH", "min-salary"] = df.loc[df["RateInterval"] == "PH", "min-salary"] * 2080
    df.loc[df["RateInterval"] == "PH", "max-salary"] = df.loc[df["RateInterval"] == "PH", "max-salary"] * 2080
    df.to_csv('cleaned_jobs.csv')
    print(df.loc[df["RateInterval"] == "PH"])

