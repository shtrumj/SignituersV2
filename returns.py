import json
# from flatten_json import flatten
import pprint

import pandas as pd
import time
from faker import Faker, Faker
import numpy as np

input_json = 'myJson.json'
indict = {}
# input_dict = json.loads(input_json)
df = pd.read_json(input_json)


# input_dict = json.loads(input_json)

# print(input_dict)


def get_second():
    first = len(df['publications'])
    indict = {'type':[], 'value':[]}
    maxsec = {"max": [], "second": []};
    conty = 0
    for max in range(0, first):
        sec =len(df['publications'][max]['indicators'])
        maxsec = {"max": max, "second":sec}
        # pprint.pprint(maxsec)
        for x in maxsec:
            county = conty + 1
            # print(max, sec)
            pprint.pprint((df['publications'][max]['indicators'][sec-1]))
        print("conty value is :", conty)
    return


get_second()
