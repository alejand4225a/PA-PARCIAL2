from smtplib import SMTP
from email.message import EmailMessage
from config import settings
message = EmailMessage()

message ['Subject'] = 'prueba para enviar email'
message['From'] = 'fefrwgregerg'
message['To'] = 'luismoraj641@gmail.com'
message.set_content('prueba')

username = settings.SMTP_USERNAME
password = settings.SMTP_PASSWORD

server = SMTP(settings.SMTP_HOSTNAME)
server.starttls()
server.login(username,password)
server.send_message(message)
print(username,password)
server.quit()