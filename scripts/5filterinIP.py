import re

f = open("../DataFiles/RawData/MyList.txt", "r")

data = f.read()

IPAddresses = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', data)

# print(IPAddresses)


with open ("../DataFiles/IPaddresses.txt", 'w') as md:
     for line in IPAddresses:
         md.write("%s\n" % line)
