import docx
import docx2txt
import json
from html import escape
# a = []

a = 0
# doc = docx.Document("Leads.docx")
# print(doc.paragraphs)
# with open("Leads.docx", encoding="utf-8", mode='rb') as f:
    # for line in f.readlines():
    #     print(u"{}".format(line) + '   ---\n')
    #     a = 0

r = """{,"price":20.750,"price_after_item_discount":20.750,"price_after_order_discount":21.580,"product_id":"193444620597","product_name":"\xd8\xac\xd8\xa7\xd9\x83\xd9\x8a\xd8\xaa \xd8\xaa\xd8\xb4\xd8\xa7\xd9\x84\xd9\x86\xd8\xac\xd8\xb1 3 \xd9\x84\xd9\x84\xd8\xb1\xd8\xac\xd8\xa7\xd9\x84","quantity":1}"""
print(json.loads(escape(r)))
