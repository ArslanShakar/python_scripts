import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysql.connector as mysql

RECEIVER_EMAIL = 'alifarslan786@gmail.com'  # REPLACE YOUR MAIL
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
     table {
     background: white;
     border-radius:3px;
     border-collapse: collapse;
     height: auto;
     max-width: 900px;
     padding:5px;
     width: 100%;
     animation: float 5s infinite;
     }
     th {
     color:#D5DDE5;;
     background:#1b1e24;
     border-bottom: 4px solid #9ea7af;
     font-size:14px;
     font-weight: 300;
     padding:10px;
     text-align:center;
     vertical-align:middle;
     }
     tr {
     border-top: 1px solid #C1C3D1;
     border-bottom: 1px solid #C1C3D1;
     border-left: 1px solid #C1C3D1;
     color:#666B85;
     font-size:16px;
     font-weight:normal;
     }
     tr:hover td {
     background:#4E5066;
     color:#FFFFFF;
     border-top: 1px solid #22262e;
     }
     td {
     background:#FFFFFF;
     padding:10px;
     text-align:left;
     vertical-align:middle;
     font-weight:300;
     font-size:13px;
     border-right: 1px solid #C1C3D1;
     }
     </style>
     </head>
     <body>
     Dear,<br> <br>
     <table>
     <thead>
     <tr style="border: 1px solid #1b1e24;">
     <th>head1</th>
     <th>head2</th>
     </tr>
     </thead>
     <tbody>
     <tr>
     <td>{}</td>
     </tr>
     </tbody>
     </table>
     <br>
     <br>
     Please Login here:
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
        message['From'] = SENDER_EMAIL
        message['To'] = RECEIVER_EMAIL
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
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()


if __name__ == '__main__':
    SendEmail()
