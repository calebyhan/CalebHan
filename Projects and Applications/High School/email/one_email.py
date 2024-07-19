'''
Emails
Author: Caleb Han
'''

# imports
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# server/port
smtp_server = 'smtp.gmail.com'
port = 465

# input sending/recieving emails
sender = ''
password = input('Enter your password here: ')
receiver = ''

message = MIMEMultipart('alternative')
message['Subject'] = 'Multipart Test'
message['From'] = sender
message['To'] = receiver

# sample email to send
text = """\
Hi, 
How are you?
fsdfijsidfjsodi
www.gmail.com
"""

# sample html to send
html = """\
<html>
    <body>
        <p>Hi, <br>
            How are you?<br>
            <a href="https://www.google.com/">Google</a>
            has many great info.
        </p>
    </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
