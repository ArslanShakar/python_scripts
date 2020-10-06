import re
import json


def clean_json(text):
    for c in ['\r\n', '\n\r', u'\n', u'\r', u'\t', u'\xa0']:
        text = text.replace(c, ' ')
    return re.sub(' +', '', text).strip()


data = clean_json(''.join(open("example.json").readlines()))
data = data.replace(',}', '}')
data = json.loads(data)

for store in data['store']:
    print store
    print(store['StoreID'])
    print(store['StoreName'])
    print(store['StoreLocation'])
    print('\n')

