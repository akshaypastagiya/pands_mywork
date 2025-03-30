#sendmai.py
#aurther:Akshay Pastagiya
#send an email via gmail
#Send email with your Name and Age

import smtplib
from email.mime.text import MIMEText

name = input("what is your Name? ")
age = input("What is your age? ")

subject = "Introduction"
body = (f"Hello {name} \n Your age is {age}.")
sender = "akshay17186@gmail.com"
recipients = ["G00473015@atu.ie"]
password = "cvotwqnjlfowbinh12345"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)