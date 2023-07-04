import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from dotenv import load_dotenv
load_dotenv()

PORT = 587
EMAIL_SERVER = "smtp.office365.com"

sender_email = os.getenv('EMAIL')
email_pw = os.getenv('PASSWORD')

def send_emails(subject, name, recipient_email, species, rare_bird, location_name, date):
    # Create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Bird Observer, LLC", f"{sender_email}"))
    msg["To"] = recipient_email

    msg.set_content(
        f"""\
        Hey, {name}!
        A {species} has been spotted at {location_name} on {date}!
        Rare bird?: {rare_bird}
        """
    )

    # HTML version. This converts the message into a multipart/alternative
    # container, with the original message as the first part and the new HTML
    # message as the second part.
    msg.add_alternative(
        f"""\
        <html>
            <body>
                <h1>Hey, {name}!</h1>
                <p>A {species} has been spotted at {location_name} on {date}!</p>
                <p>Rare bird?: {rare_bird}</p>
            </body>
        </html>
        """,
        subtype="html"
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, email_pw)
        server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == "__main__":
    send_emails(
        subject="",
        name="",
        recipient_email="",
        species="",
        rare_bird="",
        location_name="",
        date=""
    )