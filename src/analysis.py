import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('/Users/amadoubarrie/Desktop/job-market-pipeline/data/cleaned/cleaned_jobs.csv')

data.to_csv("final_jobs.csv", index=False)

results = data.groupby('Organization')['max-salary'].mean().sort_values(ascending = False)


location_results =data['Location'].value_counts().sort_values(ascending= False)
print(location_results)


sns.barplot(x=results.values, y=results.index)
plt.title("Top Highest Paying Organizations")
plt.xlabel("Average Max Salaries")
plt.ylabel("Organizations")
plt.tight_layout()

sns.barplot(x=location_results.values, y=location_results.index)
plt.title("Top Locations of the highest paying Organizations")
plt.xlabel("Location count")
plt.ylabel("Organizations")
plt.tight_layout()
plt.show()


# sns.histplot(data=data, x="max-salary")
# plt.show()