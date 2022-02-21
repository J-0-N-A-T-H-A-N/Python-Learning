import requests
import datetime as dt

endpoint = "http://api.open-notify.org/iss-now.json"    # ISS API

response = requests.get(url=endpoint)
response.raise_for_status()

iss_location = response.json()
print(iss_location)
longitude = iss_location["iss_position"]["longitude"]
latitude = iss_location["iss_position"]["latitude"]
time = dt.datetime.fromtimestamp(iss_location["timestamp"])
iss_position = (longitude, latitude)
print(f"{time}: {iss_position}")
