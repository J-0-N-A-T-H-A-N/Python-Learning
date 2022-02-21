import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = 51.8700
MY_LONG = -8.35206
SMTP_SERVER = "smtp.live.com"
FROM_EMAIL = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxxxxxxxxxx"


def is_it_dark():
    sun_endpoint = "https://api.sunrise-sunset.org/json"
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url=sun_endpoint, params=params)
    response.raise_for_status()
    current_time = datetime.now()
    # current_time = datetime.strptime("2022-01-06 03:04:17.752658", '%Y-%m-%d %H:%M:%S.%f')  # Make it dark
    sun_data = response.json()
    sunrise_hour = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = sun_data["results"]["sunset"].split("T")[1].split(":")[0]
    if current_time.hour < int(sunrise_hour) or current_time.hour > int(sunset_hour):
        return True


def iss_overhead():
    iss_endpoint = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=iss_endpoint)
    response.raise_for_status()
    iss_long = float(response.json()["iss_position"]["longitude"])
    iss_lat = float(response.json()["iss_position"]["latitude"])
    # iss_long = -8    # These 2 linces put the ISS overhead
    # iss_lat = 56
    lat_min = int(MY_LAT) - 5
    lat_max = int(MY_LAT) + 5
    long_min = int(MY_LONG) - 5
    long_max = int(MY_LONG) + 5
    if iss_long in range(long_min, long_max + 1) and iss_lat in range(lat_min, lat_max + 1):
        return True


while True:
    if is_it_dark() and iss_overhead():
        print("Quick, the ISS is overhead, check outside!")
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=FROM_EMAIL,
                                to_addrs="jonathan_garvin@hotmail.com",
                                msg="Subject:ISS OVERHEAD\n\n\n Check outside, the International Space Station is "
                                    "currently passing overhead and it should be dark enough to see"
                                )
    elif not is_it_dark() and iss_overhead():
        print("The ISS is overhead, but it's not dark enough to see")
    else:
        print("No sign of the Space Station yet, or it's too light to see!")

    sleep(60)
