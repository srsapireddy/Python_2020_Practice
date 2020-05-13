import smtplib as mail

mailserver = mail.SMTP("example.net")
mailserver.login("testuser","testpassword")

msg = '''
From: <sender@example.net>
To: <recipient@example.net>
Subject: A Test email Message!
html-content: text/html
MIMI-version: 1.0

This is a text message.
'''

mailserver.sendmail("sender@example.net","recipient@example.net",msg)
