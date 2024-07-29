import time
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import os

load_dotenv()

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)

    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")
    
    print(f"GMAIL_USER: {gmail_user}")
    print(f"GMAIL_PASSWORD: {gmail_password}")

    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=gmail_user, password=gmail_password)
    connection.send_message(msg)
    connection.quit()

if __name__ == '__main__':
    email_alert("Testing","https://www.linkedin.com/in/nelly-ayebale-4864b0202/","ayebalenelly26@gmail.com")