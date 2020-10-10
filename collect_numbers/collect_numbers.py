import re

numbers_re = re.compile(r'[+][0-9 ]+')

num_txt_file = open("funeral_numbers.txt", mode='a')
num_csv_file = open("funeral_numbers.csv", mode='a')
num_csv_file.write('Number\n')

phones = []

with open('chat3.txt', mode='r') as f:
    for line in f.readlines():
        results = numbers_re.findall(line)

        for ph in results:
            ph = ph.strip()
            if not ph or ph in phones or len(ph) < 9:
                continue
            phones.append(ph)
            num_txt_file.write(ph + '\n')
            num_csv_file.write(ph + '\n')
