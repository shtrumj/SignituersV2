import requests
import json
import urllib.request
url = "https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00"

payload={}
headers = {
  'CN-USER-NAME': 'soc_trot',
  'X-API-KEY': '1E804161881901AB',
  'Authorization': 'Basic Og==',
  'Cookie': 'LastMRH_Session=b8c05467; MRHSession=1da3978fd1960afc055af4c9b8c05467'
}

response = requests.request("GET", url, headers=headers, data=payload)

myjson =response.text

with open("myJson.json", "w", encoding='utf-8') as outfile:
  json.dump(response.json(), outfile)