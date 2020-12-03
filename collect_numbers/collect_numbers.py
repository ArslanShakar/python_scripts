import re
from datetime import datetime

numbers_re = re.compile(r'[+][0-9 ]+')

today = datetime.now().strftime('%d%b%y')
num_txt_file = open(f"output/funeral_numbers_{today}.txt", mode='w')
num_csv_file = open(f"output/funeral_numbers_{today}.csv", mode='w')
num_csv_file.write('Number\n')

files = [
    'WhatsApp Chat with (عزاءالمرحومة وداد خريبط)',
    'WhatsApp Chat with عزاء الحاج حمد جواد بوحمد',
    'WhatsApp Chat with عزاء الحاج عبدالصمد دشتي ',
    'WhatsApp Chat with عزاء الحاج محمد أشكناني',
    'WhatsApp Chat with عزاء الحاج منصور الصحاف',
    'WhatsApp Chat with عزاء السادة الخباز القلاف',
    'WhatsApp Chat with عزاء الشواف و المويل',
    'WhatsApp Chat with عزاء الصالح - رجال',
    'WhatsApp Chat with عزاء القطان و الجريدان',
    'WhatsApp Chat with عزاء المرحوم نادر الخضري',
    'WhatsApp Chat with عزاء بارون و اشكناني ',
    'WhatsApp Chat with عزاء بدريه الخضري_ القطان',
    'WhatsApp Chat with عزاء سعيد بلال المرشد',
    'WhatsApp Chat with عزاء عميد آل المتروك',
    'WhatsApp Chat with عزاء فاضل الصايغ الغالي',
    'WhatsApp Chat with عزاء والد د.بدر الخضري',
    'WhatsApp Chat with عزاءآل بوصخرالاحبة الكرام',
    'WhatsApp Chat with عزاءآل معرفي الاحبةالكرام',
    'WhatsApp Chat with عزاءالنجدي وعبدعلي الكرام',
    'WhatsApp Chat with ◼️عزاء المعراج◼️',
]
phones = []

for filename in files:
    print(filename)
    with open(f'{filename}.txt', mode='r') as f:
        for line in f.readlines():
            results = numbers_re.findall(line)

            for ph in results:
                ph = ph.strip()
                if not ph or ph in phones or len(ph) < 9 or '+965' not in ph:
                    continue
                phones.append(ph)
                num_txt_file.write(ph + '\n')
                num_csv_file.write(ph + '\n')
