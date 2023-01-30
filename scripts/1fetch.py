import requests
import json
import os
from dotenv import load_dotenv,find_dotenv

env_file= find_dotenv(".env.api_fetch")
load_dotenv(env_file)
file_path = 'DataFiles/RawData/myJson.json'
url = "https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00"

payload={}
headers = {
  'CN-USER-NAME': os.getenv("API_USER"),
  'X-API-KEY': os.getenv("API_KEY"),
  'Authorization': 'Basic Og==',
  'Cookie': 'LastMRH_Session=b8c05467; MRHSession=1da3978fd1960afc055af4c9b8c05467',
  'Content-type': 'application/json; charset=utf-8'
}

response = requests.request("GET", url, headers=headers, data=payload)
response_formated =response.json()

myjson = json.dumps(response_formated, ensure_ascii=False)
# file = "../DataFiles/RawData/myJson.jsonson"
mode = 'a' if os.path.exists(file_path) else 'w'
with open(file_path, mode, encoding='utf-8') as outfile:
  json.dump(response.json(), outfile, ensure_ascii=False)
