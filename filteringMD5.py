import re

f = open("MyList.txt", "r")

data = f.read()

md5 = re.findall(r"([a-fA-F\d]{32})", data)
with open ("md5", 'w') as md:
    for line in md5:
        md.write("%s\n" % line)
