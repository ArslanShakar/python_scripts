# -*- coding: utf-8 -*-

import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


user_email = 'Diego@innovativegx.com'
password = 'ForTesting101!'

SENDER_EMAIL = 'huwaiguest@gmail.com'  # REPLACE YOUR MAIL
SENDER_PASSWORD = 'huwai78600'  # REPLACE YOUR PASSWORD

port = 587
SERVER = 'smtp.gmail.com:{}'.format(port)
RECEIVER_EMAIL = 'alifarslan786@gmail.com'  # REPLACE YOUR MAIL

SUBJECT = 'Pending Orders Notification'

HTML_T = """
     <!DOCTYPE html>
     <html>
     <head>
     <meta charset="utf-8" />
     <style type="text/css">
     </style>
     </head>
     <body>
     Dear Diego,<br> <br>
     <h3>{}</h3>
     <br>
     For checking pending orders please login here:
     <a href='https://us.elabinventory.com/login/'>eLabInventory</a>.<br> <br>
     Thank you!
     </body>
     </html>"""


class CheckPendingOrders:
    driver = Chrome(ChromeDriverManager().install())
    driver.get("https://us.elabjournal.com/")
    time.sleep(3)

    if 'cancelRedirect' in driver.page_source:
        driver.find_element_by_id("cancelRedirect").click()
        time.sleep(0.5)
    driver.find_element_by_name("email").send_keys(user_email)
    time.sleep(0.5)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_id("loginbutton").click()
    time.sleep(7)

    pending_orders_url = "https://us.elabjournal.com/members/inventory/ordering/?order_status=PENDING#sortColumn=elab_date_entered&sortDirection=DESC"
    driver.get(pending_orders_url)
    time.sleep(7)

    def _generate_message(self, html):
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message['Subject'] = SUBJECT
        message['From'] = SENDER_EMAIL
        message['To'] = RECEIVER_EMAIL
        return message

    def send_message(self):
        server = smtplib.SMTP("smtp.gmail.com", port)
        text = "Please login into eLABInventory. You have pending orders available in the que to approve."

        html = HTML_T.format(text)
        message = self._generate_message(html)

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
        print(text)


if __name__ == "__main__":
    obj = CheckPendingOrders()

    try:
        while True:
            if "helperTableRow" in obj.driver.page_source and "rowSelector" in obj.driver.page_source:
                obj.send_message()
            time.sleep(60 * 1)
            obj.driver.get(obj.pending_orders_url)
            time.sleep(7)

    except Exception as e:
        obj.driver.close()
        print(e)
