import requests
import json
import urllib.request
from pathlib import Path
import os

writepath = 'DataFiles/RawData/myJson.json'



url = "https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00"

payload={}
headers = {
  'CN-USER-NAME': 'soc_trot',
  'X-API-KEY': '1E804161881901AB',
  'Authorization': 'Basic Og==',
  'Cookie': 'LastMRH_Session=b8c05467; MRHSession=1da3978fd1960afc055af4c9b8c05467'
}

response = requests.request("GET", url, headers=headers, data=payload)
response2 =response.json()


myjson = json.dumps(response2, ensure_ascii=False)
# file = "../DataFiles/RawData/myJson.jsonson"
mode = 'a' if os.path.exists(writepath) else 'w'
with open(writepath, mode) as outfile:
  json.dump(response.json(), outfile)
# with open(file, "w+", encoding='utf-8') as outfile:
#   json.dump(response.json(), outfile)