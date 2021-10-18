from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv


def send_email(email, commuteTime, average_time, count):
    from_email = 'GMAIL EMAIL ADDRESS HERE'
    from_password = 'PASSWORD HERE'
    to_email = email

    subject = "Height data"
    message = "Hi there! Your height is <strong>%s</strong> <strong>cm</strong>. " \
              "Average height of all users is <strong>%s</strong> <strong>cm</strong> and that " \
              "is calculated out of <strong>%s</strong> participants.<br><br> " \
              "Sincerely,<br>Webapps Business" % (commuteTime, average_time, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)