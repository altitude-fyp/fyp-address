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

@app.get("/api/email/{receiver_email}")
def email(receiver_email: str):

    status = "success"

    try:
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("EMAIL_PASSWORD")

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "This is a test email sent from fyp-address backend"

        message_content = f"""hello this email is sent from {sender_email}"""

        message.attach(MIMEText(message_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls() #enable security
        session.login(sender_email, sender_password) #login with mail_id and password
        
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()

    except Exception as err:
        status = str(err)

    return {
        "sender email": os.getenv("EMAIL"),
        "receiver email": receiver_email,
        "message": text,
        "status": status
    }