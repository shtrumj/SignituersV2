import pprint
import pandas as pd
input_json = '../DataFiles/RawData/myJson.json'
indict = {}

df = pd.read_json(input_json)
def jsonFlat():
    first = len(df['publications'])
    indict = {'type':[], 'value':[]}
    maxsec = {"max": [], "second": []};
    conty = 0
    for max in range(0, first):
        sec =len(df['publications'][max]['indicators'])
        maxsec = {"max": max, "second":sec}
        MyDictionary = {"type":[], "value":[]}
        newDict = dict()
        MyDictionary.clear()
        temp = []
        domains = []
        for x in maxsec:
            value, type =(df['publications'][max]['indicators'][sec-1]["value"],df['publications'][max]['indicators'][sec - 1]["type"])
            # MyDictionary["value","type"] = value,type
            MyDictionary.update({'value':value, 'type':type})
            # print(MyDictionary['type']
            for key, value in MyDictionary.items():
                if value == 'domain':
                    # print(MyDictionary['value'])
                    domains.append(str(MyDictionary['value']))
                    # print(domains)
                    with open("../DataFiles/domains.txt", 'a') as md:
                        for line in domains:
                            md.write("%s\n" % line)

    return







jsonFlat()
