# -*- coding: utf-8 -*-

from csv import DictReader

headers = ["placement_id", "beacon_name", "count"]
output_file = open("beacon_count_results_vertical.csv", mode='w')
output_file.write(','.join(headers) + '\n')

beacon_names_count = {}
file_name = "output_count_results.csv"

for r in DictReader(open(file_name)):
    r = dict(r)
    if not r or r['beacon_name'] == 'beacon_name':
        continue

    beacon_names_count.setdefault(r['beacon_id'], {})
    beacon_names_count[r['beacon_id']].setdefault(r['beacon_name'].strip(), 0)
    beacon_names_count[r['beacon_id']][r['beacon_name'].strip()] += 1

for placement_id, bnc in beacon_names_count.items():
    for name, count in bnc.items():
        output_file.write(','.join([placement_id, name, str(count)]) + '\n')
