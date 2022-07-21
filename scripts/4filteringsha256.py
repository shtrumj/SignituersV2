import re

f = open("DataFiles/RawData/MyList.txt", "r")

data = f.read()

sha256 = re.findall(r'[A-Fa-f0-9]{64}', data)


with open ("DataFiles/sha256.txt", 'w') as md:
     for line in sha256:
         md.write("%s\n" % line)
