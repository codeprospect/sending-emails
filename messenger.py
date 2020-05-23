import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['youremailaddress@gmail.com', 'myemailaddress@gmail.com', 'hisemailaddress@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'This your dream car'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content ('This....')

#here we are using the separate html file instead of using the tripple quotes
with open('email.html', 'rb') as f:
    file_data = f.read()
    file_name = f.name

file_string = file_data.decode(encoding='UTF-8')

msg.add_alternative(file_string, subtype='html')


'''
- How we attach images to the email
- If images are several we can use a for loop

with open('example.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
'''

'''
- How we attach pdf to the email

with open('example.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

'''

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
