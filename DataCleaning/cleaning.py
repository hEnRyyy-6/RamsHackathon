
import json 
import pandas as pd
from datetime import datetime

with open('/Users/henryvelasquez/RamsHackathon/RamsHackathon/Copy of RAMHACK CASEFILES 3/incident_reports.json', 'r') as f:
    incident_reports = json.load(f)
incident_reports_df = pd.json_normalize(incident_reports)
incident_reports_df.to_csv('cleaned_incident_reports.csv', index=False)
print(incident_reports_df)

with open('/Users/henryvelasquez/RamsHackathon/RamsHackathon/Copy of RAMHACK CASEFILES 3/phone_pings.json') as f:
    phone_pings = json.load(f)
print(phone_pings)

with (open('/Users/henryvelasquez/RamsHackathon/RamsHackathon/Copy of RAMHACK CASEFILES 3/suspects.json')) as f:
    suspects = json.load(f)
print(suspects)