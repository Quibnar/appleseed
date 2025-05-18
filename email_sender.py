
import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body, sender_email, smtp_settings):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL(smtp_settings['host'], smtp_settings['port']) as server:
        server.login(sender_email, smtp_settings['password'])
        server.send_message(msg)
