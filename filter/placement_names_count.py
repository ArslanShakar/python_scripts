from datetime import datetime

output_file = open("Imp Count by Placement Name.csv", mode='w')
output_file.write(','.join(['placement_name', 'placement_name - count'])+'\n')

output_file_2 = open("Imp Count by Placement ID.csv", mode='w')
output_file_2.write(','.join(['placement_id', 'placement_id - count'])+'\n')


input_text_file_name = 'data.txt'
placement_names_count = {}
headers = []

with open(input_text_file_name, mode='r') as file:
    for index, line in enumerate(file):
        values = line.split('\t')
        if index > 0:
            hour = datetime.utcfromtimestamp(int(values[1])).strftime("%I %p")
            if hour in ['09 PM', '10 PM', '11 PM', '12 PM', '01 AM', '02 AM', '03 AM', '04 AM', '05 AM']:
                print('Record is not counted due to "ts" between 9PM and 5AM : {}'.format(hour))
                continue

            r = {h: v for h, v in zip(headers, values)}
            if r['event'].lower() != 'imp':
                continue
            placement_names_count.setdefault(r['placement_id'], {})
            placement_names_count[r['placement_id']].setdefault(r['placement_name'].strip(), 0)
            placement_names_count[r['placement_id']][r['placement_name'].strip()] += 1
        else:
            headers = values


for placement_id, bnc in placement_names_count.items():
    imp_count_by_pid = 0
    for name, count in bnc.items():
        imp_count_by_pid += count
        output_file.write(','.join([name, str(count)]) + '\n')

    output_file_2.write(','.join([placement_id, str(imp_count_by_pid)]) + '\n')

