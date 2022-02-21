import os
import requests
import datetime as dt
from twilio.rest import Client

#Twilio details
account_sid = "ACf703f5ef03084ce4cb0dc0c58bcf1c6e"
auth_token = os.environ.get("AUTH_TOKEN")   #96da4afea68106cbdb26f608f049af9b

api_key = os.environ.get("OWM_API_KEY")
print(api_key)
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "appid": api_key,
    "lat": "51.87",
    "lon": "-8.35206",
    "exclude": "current,minutely,daily"
}

response = requests.get(url=endpoint, params=params)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]
print(hourly_data)
will_rain = False
for hour_data in hourly_data:
    weather_id = hour_data["weather"][0]["id"]
    timestamp = hour_data["dt"]
    time = dt.datetime.utcfromtimestamp(timestamp)
    # print(weather_id)
    if weather_id < 700:
        will_rain = True
if will_rain:
    pass
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #     body="It might rain, grab a brolly",
    #     from_="+18646614174",
    #     to="+353863890220"
    # )

    # print(message.status)
