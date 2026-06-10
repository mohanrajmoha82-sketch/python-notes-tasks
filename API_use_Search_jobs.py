import requests
import re
#get the API
response = requests.get( "https://remotive.com/api/remote-jobs")
#jion the API address
data = response.json()
#search the jobs
jobs = data["jobs"]
for job in jobs:
    print("compay name")
    print(job["company_name"])
    print("tittle")
    print(job["title"])
    print(job["salary"])
    a=re.sub(r"<.*?>","",job["description"])
    print(a)
    print("End".center(30,"*"))

