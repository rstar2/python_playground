import smtplib

# create for TLS Encryption
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# create for SSL Encryption
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtpObj.set_debuglevel(1)


# establish connection - say "HELLO"
smtpObj.ehlo()
# should return tuple (220, ....) 220 -is for SUCCESS

# if on TLS
# # smtpObj.starttls()
# # should return tuple (250, ....) 250 - is for READY

# login with the "sending" user
me = 'rumenn@qnext.com'
password = 'cadb12new'
smtpObj.login(me, password)
# should return tuple (235, ....) 235 - is for ACCEPTED

#  send the email
me = 'rumenn@qnext.com'
to = ['rstar@abv.bg']
cc = ['rstar2@abv.bg']
bcc = ['rumenn@qnext.com']

email = '''From: Rumen Neshev
To: {}
CC: {}
BCC: {}
Subject: testing
This is a test message
'''.format(','.join(to), ','.join(cc), ','.join(bcc))

smtpObj.sendmail(me, to + cc + bcc, email)
# should return dict with users to which sending failed

#  disconnect
smtpObj.quit()
# should return tuple (221, ....) 221 - is for CLOSED
