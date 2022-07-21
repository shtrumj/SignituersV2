import re

f = open("../DataFiles/RawData/MyList.txt", "r")

data = f.read()

sha1 = re.findall(r'\b[0-9a-f]{40}\b', data)

print(sha1)
with open ("../DataFiles/sha1.txt", 'w') as md:
     for line in sha1:
         md.write("%s\n" % line)
