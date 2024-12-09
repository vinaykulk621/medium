import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def attach_file(file, email):
    """attaching the file to email"""
    try:
        with open(file, "rb") as f:
            file_content = f.read()
            file_name = os.path.basename(file)
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(file_content)
            attachment.add_header(
                "content-disposition", "attachment", filename=file_name
            )
            encoders.encode_base64(attachment)
            email.attach(attachment)
    except Exception as e:
        print(f"could not attach file(s) to the email, err: {e}")
        exit(1)

    return email


def send_mail(email):
    """send email notification"""
    email["Subject"] = "Email Subject"
    email["From"] = "jon@example.com"
    email["To"] = "doe@example.com"
    email["Cc"] = "mary@example.com"
    email["Bcc"] = "jack@example.com"

    try:
        with smtplib.SMTP("smtphost.example.com", 25) as server:
            server.starttls()
            server.send_message(email)
    except Exception as e:
        print(f"could not send email, err: {e}")
        exit(1)


def main():
    email = MIMEMultipart()
    email_body = MIMEText("Important csv data sharing to you.\n\nRegards")
    email.attach(email_body)
    email = attach_file("data.csv", email)
    send_mail(email)
