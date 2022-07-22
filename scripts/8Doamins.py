import json

import pandas as pd
DomainOutputFile = '../DataFiles/domains.txt'
sha1outputFile = '../DataFiles/sha1.txt'
with open("../DataFiles/RawData/myJson.json") as f:
    data = json.load(f)
# df = pd.DataFrame(data['publications'])
data = data['publications']
df = pd.DataFrame(data)
EMList = []
filterd = []
finalDomains = []
finalNoBtackets = []
norm = pd.json_normalize(data=data)
stop = norm.index.stop
sha1= []

for first in range(0,stop):
    EMList.append(norm.indicators[first])


for list in EMList:
    for num in list:
        if num["type"] == "domain":
            finalDomains.append(num['value'])

for list in EMList:
    for num in list:
        if num["type"] == "sha1":
            sha1.append(num['value'])


with open(DomainOutputFile, 'w') as output:
    for z in finalNoBtackets:
        output.writelines("%s\n" % z)


with open(sha1outputFile, 'w') as sha1out:
    for sha in sha1:
        sha1out.writelines("%s\n" % sha)


