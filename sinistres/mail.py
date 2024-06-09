import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from configparser import ConfigParser
from email.utils import formatdate


def send_email_with_attachment(client, to_emails,
                                file_to_attach):
    mail_content =  '''Bonjour,
    voici ci joint votre devis au nom de '''+ client
    #The mail addresses and password
    sender_address = 'lessinistres2022@gmail.com'
    sender_pass = 'azerty123*'
    receiver_address = to_emails
#Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'devis assurance les sinistres'   #The subject line
#The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    filename = file_to_attach+".pdf"  # In same directory as script
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
# Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

# Add attachment to message and convert message to string
    message.attach(part)
#Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent******************')
if __name__ == "__main__":
    send_email_with_attachment("sirine", "sirinekraiem2016@gmail.com","form")