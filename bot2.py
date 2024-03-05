import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


send_from = 'toriopubgmobile@gmail.com'
send_to = 'alihandosmaganbetov@gmail.com'
subject = 'Отправка файла Excel'
message = 'Привет, во вложении находится Excel файл.'
file = 'C:\\Users\\77477\\Documents\\skcu\\Alex_2024-03-05_132.xlsx'
server = 'smtp.gmail.com'
port = 587
username = 'toriopubgmobile@gmail.com'
password = 'arww xoav rmgw nuyu'
use_tls = True


def send_email(send_from, send_to, subject, message, file, server, port, username, password, use_tls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
    msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

send_email(send_from, send_to, subject, message, file, server, port, username, password, use_tls)
