# Hotmail: smtp.live.com
# Gmail: smtp.gmail.com
# Outlook: outlook.office365.com

import smtplib

SMTP_SERVER = "smtp.live.com"  # hotmail
from_email = "xxxxxxxxxxxxxxxxxxxxxxx"
password = xxxxxxxxxxxxxxxxxxxxxxx# App password for hotmail
to_email = "xxxxxxxxxxxxxxxxxxxxxxx"

with smtplib.SMTP(SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=from_email, password=password)
    connection.sendmail(
        from_addr=from_email,
        to_addrs=to_email,
        msg="Subject: Hello from Python\n\nThis is an email sent from a python script"
    )
