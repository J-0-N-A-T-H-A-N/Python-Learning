import requests
from datetime import datetime

MY_LAT = 51.8700
MY_LONG = -8.35206

endpoint = "https://api.sunrise-sunset.org/json"
params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()

current_time = datetime.now()
# current_time = datetime.strptime("2022-01-06 03:04:17.752658", '%Y-%m-%d %H:%M:%S.%f')
sun_data = response.json()
sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunrise_min = sunrise.split("T")[1].split(":")[1]
sunset_hour = sunset.split("T")[1].split(":")[0]
sunset_min = sunset.split("T")[1].split(":")[1]

if current_time.hour < int(sunrise_hour) or current_time.hour > int(sunset_hour):
    print("It's dark")
else:
    print("It's too light")