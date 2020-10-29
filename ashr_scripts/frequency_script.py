# -*- coding: utf-8 -*-

from csv import DictReader

output_file = open("output_count_results.csv", mode='w')
file_name = "count_result.csv"
is_headers = True
seen_ids = []


for r in DictReader(open(file_name)):
    r = dict(r)
    if r['person_id'] == 'person_id' or int(r['freq']) > 10:
        continue
    if is_headers:
        is_headers = False
        output_file.write(','.join(r.keys()) + '\n')
        print(r)

    if r['person_id'] + 'c' not in seen_ids and r['event'].lower() == 'click':
        seen_ids.append(r['person_id'] + 'c')
        output_file.write(','.join(r.values()) + '\n')
        print(r)
    elif r['person_id'] + 'i' not in seen_ids and r['event'].lower() == 'imp':
        seen_ids.append(r['person_id'] + 'i')
        output_file.write(','.join(r.values()) + '\n')
        print(r)
