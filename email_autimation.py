import os
import smtplib
import imghdr
import pandas as pd

from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
contacts =[]

df = pd.read_csv('email.csv')
for row in df.iterrows():
    email = row[1]

    contacts.append(email[0])

print(contacts)

msg = EmailMessage()
msg['Subject'] = 'test mail-3'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('hello world. image attached and pdf attached. attempt-3')

files = ['0.png', '001.png']
attechedfile = ['study.pdf']
# for picture
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)  # passing the name of file
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# for documents
for attachment in attechedfile:
    with open(attachment, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)