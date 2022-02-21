
import datetime as dt
from pandas import *
import random
import smtplib

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day
smtp_server = "smtp.live.com"
from_email = "xxxxxxxxxxx"
from_password = "xxxxxxxxxxx"

birthday_data = read_csv("birthdays.csv")
bd_dict = birthday_data.to_dict(orient="records")

for row in range(len(bd_dict)):
    if (bd_dict[row]["month"] == current_month) & (bd_dict[row]["day"] == current_day):
        name = bd_dict[row]["name"]
        email = bd_dict[row]["email"]
        letter_num = random.randint(1, 3)
        letter = f'letter_templates\\letter_{letter_num}.txt'
        with open(letter, "r") as letter_file:
            message = letter_file.read().replace("[NAME]", name)
        with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(user=from_email, password=from_password)
            connection.sendmail(from_addr=from_email,
                                to_addrs=email,
                                msg=f"Subject: Birthday Greetings\n\n\n{message}"
                                )
        print(f"Email sent to {email}")
