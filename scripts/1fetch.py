import requests
import json
import os

file_path = '../DataFiles/RawData/myJson.json'
url = "https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00"

payload={}
headers = {
  'CN-USER-NAME': 'soc_trot',
  'X-API-KEY': '0CED85C07DA0A153',
  'Authorization': 'Basic Og==',
  'Cookie': 'LastMRH_Session=b8c05467; MRHSession=1da3978fd1960afc055af4c9b8c05467',
  'Content-type': 'application/json; charset=utf-8'
}

response = requests.request("GET", url, headers=headers, data=payload)
response2 =response.json()


myjson = json.dumps(response2, ensure_ascii=False)
# file = "../DataFiles/RawData/myJson.jsonson"
mode = 'a' if os.path.exists(file_path) else 'w'
with open(file_path, mode, encoding='utf-8') as outfile:
  json.dump(response.json(), outfile, ensure_ascii=False)
