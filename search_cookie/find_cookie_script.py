import re
from csv import DictReader

input_file_user_locations = "users and paths.csv"
user_paths = DictReader(open(input_file_user_locations))

output_file = open("output cookie values.csv", mode="w")
output_file.write("User,Path,Cookie\n")

searching_keyword = "www.linkedin.comli_at"
search_re = re.compile(searching_keyword + '(.*)/')

for user in user_paths:
    try:
        file_path = user['Path'] + "\\Cookies"
        lines = open(file_path, mode='r', encoding='utf-8', errors='ignore').readlines()
        file_text = ', '.join(lines)

        if searching_keyword not in file_text:
            print("No match result found for this keyword: %s" % searching_keyword)
            exit()

        for r in search_re.findall(file_text):
            if not (r or '').strip() or '/' not in r:
                continue

            cookie = (r or ' ').split('/')[0].strip()
            # if len(cookie) != 152:
            #     continue
            data = f"{user['User']},{user['Path']},{cookie}\n"
            output_file.write(data)
            print(data)

    except Exception as e:
        print(e)
