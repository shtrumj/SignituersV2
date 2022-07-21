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
        for x in maxsec:
            value =(df['publications'][max]['indicators'][sec-1]["value"])
            type=(df['publications'][max]['indicators'][sec - 1]["type"])
            MyDictionary["value"] = value
            MyDictionary["type"] = type
            print(dict(filter(lambda x: x[1] == 'domain',MyDictionary.values())))
            # for key, value in MyDictionary.items():
            #     if value == 'domain':
            #         print(value)

            # type_filter = [t for t in MyDictionary.items() if v =='domain']
            # print(type_filter)
            # pprint.pprint(MyDictionary["type"] == "domain")
            # for key,value in MyDictionary.items():
            #     if key == "domain":
            #         newDict[key] = value
            # print("filtered: ", newDict)
    return


jsonFlat()
