

import pandas as pd


incident_reports_df = pd.read_csv('/Users/henryvelasquez/RamsHackathon/RamsHackathon/cleaned_incident_reports.csv')


print(incident_reports_df.head())

print(incident_reports_df.describe())
print(incident_reports_df.info())

