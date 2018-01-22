import json
from pprint import pprint

data = json.load(open('C:\\Ponant\\transferPurchaseHist.json', encoding="utf8"))

#pprint(data)
#print(len(data['result'][0]['run']))
print(len(data))
print(data[26299])

print('c est fini')