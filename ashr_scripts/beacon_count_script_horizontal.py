# -*- coding: utf-8 -*-

from csv import DictReader

output_file = open("beacon_count_results_horizontal.csv", mode='w')
headers = ["placement_id"]
beacon_names_count = {}
file_name = "output_count_results.csv"

for r in DictReader(open(file_name)):
    r = dict(r)
    if not r or r['beacon_name'] == 'beacon_name':
        continue

    beacon_names_count.setdefault(r['beacon_id'], {})
    beacon_names_count[r['beacon_id']].setdefault(r['beacon_name'].strip(), 0)
    beacon_names_count[r['beacon_id']][r['beacon_name'].strip()] += 1

headers = ["placement_id"]

for pid, bnc in beacon_names_count.items():
    headers += [k for k in bnc]

output_file.write(','.join(headers) + '\n')

for placement_id, bnc in beacon_names_count.items():
    row = [placement_id] + [str(bnc.get(h, '')) for h in headers[1:]]
    output_file.write(','.join(row) + '\n')
