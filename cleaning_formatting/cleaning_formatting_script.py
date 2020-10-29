import re
from csv import DictReader

from nameparser import HumanName

punctuation_re = re.compile(r'[^\w-]')


class FileFormatting:
    input_file_name = "input code violation.csv"
    record_key = "{NAME}{SITUS_NUMBER}{SITUS_STREET}{CITY}{ZIPCODE}"

    seen_records = []
    csv_headers = [
        "Full Name", "First Name", "Last Name",
        "Property Address", "Property City", "Property ZipCode"
    ]

    output_file = open("output code violation.csv", mode="w")
    output_file.write(",".join(csv_headers) + "\n")

    def clean_rows(self):
        for row in DictReader(open(self.input_file_name)):
            if not row or row['NAME'] == 'NAME':
                continue
            key = self.record_key.format(**row).lower().strip()
            if key in self.seen_records:
                continue
            self.seen_records.append(key)

            address = [row['SITUS_NUMBER'], row['SITUS_STREET']]
            item = self.get_name_parts(row['NAME'])

            # Middle Name and Last Name -> First Name & First Name -> Last Name
            fn = item['First Name']
            item['First Name'] = "{Middle Name} {Last Name}".format(**item).strip()
            item['Last Name'] = fn

            item["Property Address"] = " ".join(s for s in address if (s or '').strip())
            item["Property City"] = row['CITY']
            item["Property ZipCode"] = row['ZIPCODE']
            self.write_to_csv(item)
            print(item)

    def get_name_parts(self, name):
        name_parts = HumanName(name)
        return {
            'Full Name': name.strip(),
            'Prefix': re.sub(punctuation_re, '', name_parts.title),
            'First Name': re.sub(punctuation_re, '', name_parts.first),
            'Middle Name': re.sub(punctuation_re, '', name_parts.middle),
            'Last Name': re.sub(punctuation_re, '', name_parts.last),
            'Suffix': re.sub(punctuation_re, '', name_parts.suffix)
        }

    def write_to_csv(self, item):
        self.output_file.write(",".join([item[h] for h in self.csv_headers]) + "\n")


if __name__ == "__main__":
    FileFormatting().clean_rows()
