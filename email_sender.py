from email.message import EmailMessage
from pass_saver import password 
import ssl
import smtplib

email_sender = 'jefficostau@gmail.com'
email_password = password

#you can get email address from https://temp-mail.org/
email_receiver = 'vorat15186@rxcay.com'

subject = 'Test'
body = """
This is a test email
"""
e_m = EmailMessage()
e_m['From'] = email_sender
e_m['To'] = email_receiver
e_m['Subject'] = subject
e_m.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, e_m.as_string())
    print('Email sent')

