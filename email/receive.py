#  could use this one, but the external 'imapclient' is easier to use
# import imaplib

import imapclient
import imaplib
import pyzmail

host = 'imap.gmail.com'
port = 993
me = 'rumenn@qnext.com'
password = 'cadb12new'

# create
server = imaplib.IMAP4_SSL(host, port=port)

# login
server.login(me, password)

# get ionto the INBOX folder
inboxFolder = server.select('INBOX')  # return tuple (typ, [data])
inboxTyp, inboxData = inboxFolder
num_msgs = int(inboxData[0])
print('{} messages in INBOX'.format(num_msgs))

# print all folders
from pprint import pprint
pprint(server.list())

server.close()
server.logout()
