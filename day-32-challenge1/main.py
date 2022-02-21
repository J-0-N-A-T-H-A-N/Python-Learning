
import datetime as dt
import random
import smtplib

quota_file = "quotes.txt"
from_email = "jonathan_garvin@hotmail.com"
from_password = "ioljbcsosvfrsmpp"
smtp_host = "smtp.live.com"                     # Hotmail
to_email = "jonathangarvintest@gmail.com"

current_date = dt.datetime.now()
day_of_the_week = current_date.weekday()        # Looking for Monday -> day 0

if day_of_the_week == 2:
    with open("quotes.txt", "r") as quotes:
        quote_lines = quotes.readlines()

    random_quote = random.choice(quote_lines)
    with smtplib.SMTP(smtp_host) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject: Monday Morning Inspiration\n\n\n{random_quote}"
        )
else:
    print("Not Monday!")