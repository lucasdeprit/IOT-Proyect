# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import json

# create message object instance
msg = MIMEMultipart()


# setup the parameters of the message
password = "canutorioiot1234"
msg['From'] = "canutorioiot@gmail.com"
msg['To'] = "canutorioiot@gmail.com"
msg['Subject'] = "rpi"

# attach image to message body
body=""
msg.attach(MIMEText(body,'plain'))
with open(r'/home/pi/IOT-Proyect/Data/data_' + datetime.today().strftime('%Y-%m-%d') + '.json') as f:  
  data = json.load(f)  
attachment = MIMEText(json.dumps(data))
attachment.add_header('Content-Disposition', 'attachment', filename= file('data_' + datetime.today().strftime('%Y-%m-%d') + '.json').read())
msg.attach(attachment)
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['canutorioiot@gmail.com'], 'canutorioiot1234')


# send the message via the server.
server.sendmail(msg['canutorioiot@gmail.com'], msg['canutorioiot@gmail.com'], msg.as_string())

server.quit()

print "successfully sent email to %s:" % (msg['canutorioiot'])
