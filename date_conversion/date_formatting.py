from datetime import datetime


def convert_date(ts_date):
    try:
        ts = int(ts_date)
        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as err:
        print("exception: {}".format(err))
        return ts_date


output_file = open("Output Results.csv", mode='w')

input_text_file_name = 'data.txt'

with open(input_text_file_name, mode='r') as file:
    for index, line in enumerate(file):
        values = line.split('\t')
        if index > 0:
            date = convert_date(values[1])
            values.insert(2, date)
            output_file.write(','.join(values))
            print(date)
        else:
            values.insert(2, "date")
            output_file.write(','.join(values))
