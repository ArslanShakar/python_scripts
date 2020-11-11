import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysql.connector as mysql

# RECEIVER_EMAIL = 'alifarslan786@gmail.com'  # REPLACE YOUR MAIL
RECEIVER_EMAILS = [
    'alifarslan786@gmail.com',
    'arslan45936@gmail.com',
    'mrarslan101@gmail.com'
    ]
SENDER_EMAIL = 'huwaiguest@gmail.com'  # REPLACE YOUR MAIL
SENDER_PASSWORD = 'huwai78600'  # REPLACE YOUR PASSWORD
SERVER = 'smtp.gmail.com:587'
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# mysql connection details

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


class SendEmail:
    def __init__(self):
        self.send_message()

    def _generate_message(self, html):
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message['Subject'] = SUBJECT
        message['From'] = "eLAB Reporting"
        message['To'] = ','.join(RECEIVER_EMAILS)
        return message

    def send_message(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        text = "Please login and check pending orders have existing in queue"
        html = HTML_T.format(text)
        message = self._generate_message(html)

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, ','.join(RECEIVER_EMAILS), message.as_string())
        server.quit()


if __name__ == '__main__':
    SendEmail()
