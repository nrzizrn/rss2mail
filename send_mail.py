#!/usr/bin/env python

# author: nrz@nullsecurity.net

import sys
import os
import re

from smtplib import SMTP_SSL
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.Encoders import encode_base64
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

from config import USERNAME
from config import PASSWORD
from config import SMTP

if not len(sys.argv) == 4:
    print "[-] Usage: %s <subject> <body> <to>" %sys.argv[0]
    sys.exit(1)
else:
    subject = sys.argv[1]
    content = sys.argv[2]
    to = sys.argv[3]

SMTPserver = SMTP
msg = MIMEMultipart()

# recipients
msg['From'] = USERNAME
msg['To'] = to

try:
    msg['Subject']= subject
    msg.attach(MIMEText(content, "plain"))
    conn = SMTP_SSL(SMTPserver, 465)
    conn.set_debuglevel(True)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(msg['From'], to, msg.as_string())
    finally:
        conn.close()

except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) )
