# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:42:21 2017

@author: LALIT ARORA
"""

import smtplib
from credentials import cred

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

fromaddr=cred.sendid()
password=cred.sendpass()

toaddr = "xxxx@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ADD SUBJECT HERE"
 
body = "ADD YOUR MESSAGE HERE"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "FILE NAME WITH EXTENSION"
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()