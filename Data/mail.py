#!/usr/bin/env python

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender_email = "canutorioiot@gmail.com"
receiver_email = "canutorioiot@gmail.com"
message = MIMEMultipart()
message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "sending mail using python"

file = 'data_' + datetime.today().strftime('%Y-%m-%d') + '.csv'
attachment = open('/home/pi/IOT-Proyect/Data/' + file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)

file2 = 'data_temp_' + datetime.today().strftime('%Y-%m-%d') + '.csv'
attachment2 = open('/home/pi/IOT-Proyect/Data/' +file2,'rb')
obj2 = MIMEBase('application','octet-stream')
obj2.set_payload((attachment2).read())
encoders.encode_base64(obj2)
obj2.add_header('Content-Disposition',"attachment; filename= "+file2)
message.attach(obj2)


file3 = 'data_humi_' + datetime.today().strftime('%Y-%m-%d') + '.csv'
attachment3 = open('/home/pi/IOT-Proyect/Data/' +file3,'rb')
obj3 = MIMEBase('application','octet-stream')
obj3.set_payload((attachment3).read())
encoders.encode_base64(obj3)
obj3.add_header('Content-Disposition',"attachment; filename= "+file3)
message.attach(obj3)

my_message = message.as_string()
email_session = smtplib.SMTP('smtp.gmail.com',587)
email_session.starttls()
email_session.login(sender_email,'canutorioiot1234')
email_session.sendmail(sender_email,receiver_email,my_message)
email_session.quit()
print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")
