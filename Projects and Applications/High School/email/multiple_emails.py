'''
Multiple email sender
Author: Caleb Han
'''

# imports
import csv, smtplib, ssl

# sample email to modify
message = """\
From: {sender}
To: {email}
Subject: Your Grades

Hi {name} your grade is {grade}.
"""

# input sending email here
sender = ''
password = input('Please enter the password: ')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    # login with email/password
    server.login(sender, password)
    # example on application of sending multiple emails
    with open('contacts.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for name, email, grade in reader:
            server.sendmail(
                sender,
                email,
                message.format(
                    sender=sender,
                    email=email,
                    name=name,
                    grade=grade,
                )
            )
