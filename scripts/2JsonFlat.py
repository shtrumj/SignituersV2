
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
        # pprint.pprint(maxsec)
        for x in maxsec:
            county = conty + 1
            # print(max, sec)
            pprint.pprint((df['publications'][max]['indicators'][sec-1]))
        print("conty value is :", conty)
    return


jsonFlat()
