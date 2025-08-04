# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

email_text = f"""
Hi! This is the report from our script.

We have added 1 + 2 and gotten the answer {1+2}.

Bye!
"""

GMAIL_USERNAME = "pizzeriatonitracker@gmail.com"
GMAIL_APP_PASSWORD = "vvxcqbaxfvklzxik"

recipients = ["loll77@hotmail.it"]
msg = MIMEText(email_text)
msg["Subject"] = "Email report: a simple sum"
msg["To"] = ", ".join(recipients)
msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
smtp_server.sendmail(msg["From"], recipients, msg.as_string())
smtp_server.quit()