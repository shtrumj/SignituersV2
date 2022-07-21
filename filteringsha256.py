import re

f = open("MyList.txt", "r")

data = f.read()

sha256 = re.findall(r'[A-Fa-f0-9]{64}', data)

print(sha256)
with open ("sha256", 'w') as md:
     for line in sha256:
         md.write("%s\n" % line)
