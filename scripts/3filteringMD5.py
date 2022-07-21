import re

f = open("DataFiles/RawData/MyList.txt", "r")

data = f.read()

md5 = re.findall(r"([a-fA-F\d]{32})", data)
with open ("DataFiles/md5.txt", 'w') as md:
    for line in md5:
        md.write("%s\n" % line)
