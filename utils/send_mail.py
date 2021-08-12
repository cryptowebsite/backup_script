import smtplib
from email.utils import make_msgid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def send_mail(text, status):
    if config.SEND_EMAIL:
        if status == 'success':
            subject = f'{config.BACKUP_NAME} backup was successfully created'
        else:
            subject = f'{config.BACKUP_NAME} backup was not created as a result of an error'

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = config.MAIL_USER
        msg['Message-ID'] = make_msgid()
        msg.attach(MIMEText(text, 'plain'))

        server = smtplib.SMTP_SSL(config.MAIL_SMTP, config.MAIL_PORT)
        server.login(config.MAIL_USER, config.MAIL_PASSWORD)
        server.sendmail(config.MAIL_USER, config.MAIL_TO, msg.as_string())
