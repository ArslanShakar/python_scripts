import re
from html import unescape

from nameparser import HumanName

csv_file = open("leads.csv", mode='w')
# csv_file.write('name,first name,last name,title,email address,company name,address,state,telephone')
csv_file.write('name,title,email address,company name,address,state,telephone,date_posted')
csv_file.write('\n')

text_file = open('leads.txt').readlines()


def get_name_parts(name):
    name_parts = HumanName(name)
    punctuation_re = re.compile(r'[^\w-]')

    return {
        'full name': name.strip(),
        'prefix': re.sub(punctuation_re, '', name_parts.title),
        'first name': re.sub(punctuation_re, '', name_parts.first),
        'middle name': re.sub(punctuation_re, '', name_parts.middle),
        'last name': re.sub(punctuation_re, '', name_parts.last),
        'suffix': re.sub(punctuation_re, '', name_parts.suffix)
    }


def clean(text):
    text = re.sub(u'"', u"\u201C", unescape(text or ''))
    text = re.sub(u"'", u"\u2018", text)
    for c in ['\r\n', '\n\r', u'\n', u'\r', u'\t', u'\xa0']:
        text = text.replace(c, ' ')
    return re.sub(' +', ' ', text).strip().title()


count = 0
item = {}

for line in text_file:
    line = clean(line)

    if not line:
        continue

    if count == 7:
        csv_file.write(','.join(item.values())+'\n')
        item = {}
        count = 0

    print(line)

    if line:
        if count == 0:
            # item['name'] = line
            item[0] = line
        elif count == 1:
            # item["title"] = line
            item[1] = line
        elif count == 2:
            # item["email address"] = line
            item[2] = line
        elif count == 3:
            # item["company name"] = line
            item[3] = line
        elif count == 4:
            # item["address"] = line
            item[4] = line
        elif count == 5:
            # item['state'] = line
            item[5] = line
        elif count == 6:
            # item['telephone'] = line
            item[6] = line
        elif count == 7:
            item[7] = line

        count += 1







