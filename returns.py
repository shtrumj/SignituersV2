import json
from flatten_json import flatten
import pprint

import pandas as pd
import time
from faker import Faker, Faker
import numpy as np

mydict = {}
df = pd.read_json("myJson.json")
#myrange = range(0, (len(df) -1))

# for lines in myrange:
#     mydict.append(df['publications'][lines]['indicators'])
#

#
# page = df['publications'][97]['indicators'][3]['type']
# print(page)
def get_first():
    first = len(df['publications'])
    return first

def get_second():
    corolation = {}
    first = get_first()
    conty = 0
    for max in range(0,first):
        # pprint.pprint(len(df['publications'][]['indicators'][202]))
        #print ('for max',max,'maximim is ',len(df['publications'][max]['indicators']))
        corolation.append({first:len(df['publications'][max]['indicators'])})

    print(corolation)
    return conty
get_second()

# for t in range(0,200):
#     pprint.pprint(len(df['publications'][first]['indicators']))

# for t in range(0,200):
#      pprint.pprint(len(df['publications']))


# df = pd.read_json("myJson.json")
# mylist =[]
# myrange = range(0, (len(df) -1))
# counter = 0

# for num in myrange:
#     mylist.append(df['publications'][num]['indicators'])
#
# print((mylist))


#print(len(newdf))
#    for line in df["indicators"]:
#         print(line)
#            counter+=1
#
# print(counter)
#data = json.load(open('myJson.json','rb'))