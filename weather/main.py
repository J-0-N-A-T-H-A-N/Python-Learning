import requests

MY_LAT = 51.8700
MY_LONG = -8.35206
WEATHER_API_KEY = "263ba91baa69e12f459edc0a7c4ad536"

def get_clouds():
    weather_endpoint = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": WEATHER_API_KEY,
    }
    response = requests.get(weather_endpoint, params=params)
    response.raise_for_status()
    json_data = response.json()
    place_name = json_data["name"]
    cloud_cover = json_data["clouds"]["all"]
    print(f"Cloud cover in {place_name} is currently {cloud_cover}")
    return cloud_cover

cloudiness = get_clouds()

print(f'Cloud cover is currently {cloudiness}%')
