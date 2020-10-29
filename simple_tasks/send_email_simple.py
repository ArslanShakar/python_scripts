# # # Python code to illustrate Sending mail from
# # # your Gmail account
# import smtplib
#
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
#
# # start TLS for security
# s.starttls()
# sender_email = "huwaiguest@gmail.com"
#
# # Authentication
# s.login(sender_email, "huwai78600")
#
# # message to be sent
# message = "Testing message sent from python script"
#
# # sending the mail
# s.sendmail(sender_email, "alifarslan786@gmail.com", message)
#
# # terminating the session
# s.quit()

##############################
#
import smtplib
SENDER_EMAIL = 'huwaiguest@gmail.com'  # REPLACE YOUR MAIL
SENDER_PASSWORD = 'huwai78600'  # REPLACE YOUR PASSWORD
SERVER = 'smtp.gmail.com:587'
RECEIVER_EMAIL = 'alifarslan786@gmail.com'  # REPLACE YOUR MAIL
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# mysql connection details


class SendEmail:
    def __init__(self):
        self.send_message()

    def send_message(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)

        message = "Sample Testing message"

        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

        server.quit()


if __name__ == '__main__':
    SendEmail()
