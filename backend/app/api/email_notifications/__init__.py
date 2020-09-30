"""
sends email notification to target_email using fypaddress@gmail.com
"""
import os
from dotenv import load_dotenv
load_dotenv()

from app import app

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

@app.get("/api/email/{receiver_email}")
def send_email(receiver_email: str):

    status = "success"

    try:
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("EMAIL_PASSWORD")

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "This is a test email sent from fyp-address backend"

        with open("app/api/email_notifications/email.html", "r", encoding="utf-8") as f:
            message_content = MIMEText(f.read(), "html")

        message.attach(message_content)
        
        with open("app/api/email_notifications/images/citilogo.png", "rb") as f:
            citilogo = MIMEImage(f.read())

        citilogo.add_header("Content-ID", "<citilogo>")
        message.attach(citilogo)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls() #enable security
        session.login(sender_email, sender_password) #login with mail_id and password
        
        message = message.as_string()
        session.sendmail(sender_email, receiver_email, message)
        session.quit()

    except Exception as err:
        status = str(err)

    return {
        "sender email": os.getenv("EMAIL"),
        "receiver email": receiver_email,
        "status": status,
    }