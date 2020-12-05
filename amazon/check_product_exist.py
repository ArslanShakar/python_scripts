# -*- coding: utf-8 -*-

import time
import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


RECEIVER_EMAIL = 'olianas.sara@gmail.com'  # REPLACE YOUR RECEIVING E-MAIL
SENDER_EMAIL = 'huwaiguest@gmail.com'  # REPLACE YOUR SENDING E-MAIL
SENDER_PASSWORD = 'huwai78600'  # REPLACE YOUR Sender Email PASSWORD

not_available_texts = [
    "Currently unavailable.", 'Non disponibile.', 'Not available.', 'No disponible.',
    'Actuellement indisponible.',
]

port = 587
SERVER = 'smtp.gmail.com:{}'.format(port)
SUBJECT = 'Amazon Product Availability Notification'

HTML_T = """
     <!DOCTYPE html>
     <html>
     <head>
     <meta charset="utf-8" />
     <style type="text/css">
     </style>
     </head>
     <body>
     Dear Olianas Sara,<br>
     <h3>The amazon product is now available for purchase.</h3>
     For buying product please click here:
     <a href='{0}'>{0}</a>.<br> <br>
     Thank you!
     </body>
     </html>"""


class CheckProductExist:
    product_links = [
        "https://www.amazon.de/-/en/dp/B08H93ZRK9/ref=twister_B08JVHJNHG?_encoding=UTF8&th=1",
        "https://www.amazon.es/PlayStation-5-Mando-inal%C3%A1mbrico-DualSense/dp/B08KKJ37F7",
        "https://www.amazon.es/PlayStation-5-Mando-inal%C3%A1mbrico-DualSense/dp/B08KJF2D25",
        "https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H93ZRK9",
        "https://www.amazon.fr/PlayStation-%C3%89dition-Standard-DualSense-Couleur/dp/B08H98GVK8",
        "https://www.amazon.it/Sony-PlayStation-5/dp/B08KJF2D25",
        "https://www.amazon.it/Sony-PlayStation-5/dp/B08KKJ37F7",
        "https://www.amazon.de/dp/B08H98GVK8",
        "https://www.amazon.de/dp/B08H93ZRK9",
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'Application/signed-exchange;v=b3;q=0.9',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-language': 'en-US,en;q=0.9',
        'Cache-control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-fetch-mode': 'navigate',
        'Sec-fetch-site': 'none',
        'Sec-fetch-user': '?1',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36'
    }

    def crawl_products(self):
        s = requests.Session()
        s.headers.update(self.headers)

        for url in self.product_links:
            print("searching link " + url)
            response = s.get(url)
            if self.is_product_not_exist(response):
                print("Product is not available yet")
            else:
                print("Congratulations! Product is now available. You can buy it.")
                obj.send_message(url)

    def _generate_message(self, html):
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message['Subject'] = SUBJECT
        message['From'] = SENDER_EMAIL
        message['To'] = RECEIVER_EMAIL
        return message

    def send_message(self, product_url):
        try:
            server = smtplib.SMTP("smtp.gmail.com", port)
            html = HTML_T.format(product_url)
            message = self._generate_message(html)

            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
            server.quit()
            print("Email has been sent to " + RECEIVER_EMAIL)

        except Exception as err:
            print(err)
            a = 0

    def is_product_not_exist(self, response):
        return sum(s in response.text for s in not_available_texts)


if __name__ == "__main__":
    obj = CheckProductExist()
    sleep_mins = 30

    try:
        while True:
            obj.crawl_products()
            print("Sleeping for {}...".format(sleep_mins))
            time.sleep(sleep_mins * 60)
    except Exception as e:
        print(e)
