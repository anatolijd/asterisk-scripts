#!/usr/bin/python
#
# Author: Anatoliy Dobrosynets, 2014
#
# Read message from pipe or cmdline and send it via 
# authenticated mail account (gmail).
# Message copy is appended to local log file.

import sys
import smtplib

to_addr   = 'sales-frontdesk@acme.com'
log_file  = '/var/log/asterisk/sms.log'
#
from_addr = 'my.mail.account54352@gmail.com'
username  = from_addr
smtp_addr = "smtp.gmail.com:587"
password  = 'gensy[eq'

# either pipe or cmdline
body = ' '.join(sys.argv[1:]) if sys.stdin.isatty() else ''.join(sys.stdin.readlines())

if not body:
    exit(0)

with open(log_file,"a") as f:
    f.write(body)

headers = '''
Content-type: text/plain
From: SMS Gate <%s>
Subject: ### %s
'''.strip() % (from_addr,"SMS")

msg = "%s\n\n%s" % (headers,body.strip())

server = smtplib.SMTP(smtp_addr,None,None,10)
server.starttls()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg)
server.quit()
