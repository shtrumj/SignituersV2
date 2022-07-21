import re

f = open("../DataFiles/RawData/MyList.txt", "r")

data = f.read()
regex = r'\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b'
#regex = r'^([a-z0-9]+(-[a-z0-9]+)*\[.])+[a-z]{2,}$'
domains = re.findall(regex, data)

print(domains)
# with open ("../DataFiles/sha1.txt", 'w') as md:
#      for line in sha1:
#          md.write("%s\n" % line)
