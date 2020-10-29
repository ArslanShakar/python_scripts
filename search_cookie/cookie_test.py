import re
# file_path = "152charactersFirst.txt"
file_path = "152charactersSecond.txt"
lines = open(file_path, mode='r', encoding='utf-8', errors='ignore').readlines()
file_text = ', '.join(lines)
searching_keyword = "www.linkedin.comli_at"
search_re = re.compile(searching_keyword + '(.*)/')

if searching_keyword not in file_text:
    print("No match result found for this keyword: %s" % searching_keyword)
    exit()

for r in search_re.findall(file_text):
    if not (r or '').strip() or '/' not in r:
        continue

    cookie = (r or ' ').split('/')[0].strip()
    # if len(cookie) != 152:
    #     continue
    print(cookie)
