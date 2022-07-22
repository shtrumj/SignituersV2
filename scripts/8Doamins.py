import json
import re
import pandas as pd
DomainOutputFile = '../DataFiles/domains.txt'
sha1outputFile = '../DataFiles/sha1.txt'
sha256Outputfile = '../DataFiles/sha256.txt'
md5Outputfile = '../DataFiles/md5.txt'
URLOutputfile = '../DataFiles/urls.txt'
IPSOutputfile = '../DataFiles/ips.txt'


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
sha256 = []
md5 = []
urls = []
ips = []
ipsNB = []
urlNB = []
urlsCl = []

for first in range(0,stop):
    EMList.append(norm.indicators[first])


for list in EMList:
    for num in list:
        if num["type"] == "domain":
            finalDomains.append(num['value'])

for list in EMList:
    for num in list:
        if num["type"] == "IP":
            ips.append(num['value'])

for list in EMList:
    for num in list:
        if num["type"] == "sha1":
            sha1.append(num['value'])


for list in EMList:
    for num in list:
        if num["type"] == "sha256":
            sha256.append(num['value'])

for list in EMList:
    for num in list:
        if num["type"] == "url":
            urls.append(num['value'])

for list in EMList:
    for num in list:
        if num["type"] == "md5":
            md5.append(num['value'])


for line in finalDomains:
    finalNoBtackets.append(re.sub(r"[\[\]]",'',line))

for line in urls:
    urlNB.append(re.sub(r"[\[\]]",'',line))


for line in urlNB:
    line= line.replace("hxxps","https")
    line=line.replace("hxxp","http")
    line = line.replace("hXXp", "http")
    urlsCl.append(line)

for line in ips:
    ipsNB.append(re.sub(r"[\[\]]",'',line))

with open(DomainOutputFile, 'w') as output:
    for z in finalNoBtackets:
        output.writelines("%s\n" % z)

with open(sha1outputFile, 'w') as sha1out:
    for sha in sha1:
        sha1out.writelines("%s\n" % sha)

with open(sha256Outputfile, 'w') as sha256out:
    for sha2 in sha256:
        sha256out.writelines("%s\n" % sha2)

with open(md5Outputfile, 'w') as md5out:
    for line in md5:
        md5out.writelines("%s\n" % line)

with open(URLOutputfile, 'w') as urls:
    for line in urlsCl:
        urls.writelines("%s\n" % line)

with open(IPSOutputfile, 'w') as ipsfile:
    for line in ipsNB:
        ipsfile.writelines("%s\n" % line)