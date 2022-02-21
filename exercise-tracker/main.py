import requests
import datetime as dt
import os

nutritionix_api_key = "1cb2e596f1964c40d2c551b59493220b"
nutritionix_app_id = "b0301c56"
user = "jon_athan"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("What exercise did you do? ")

json_data = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 89,
    "height_cm": 182,
    "age": 46
}

headers = {
    "x-app-id": "b0301c56",
    "x-app-key": "1cb2e596f1964c40d2c551b59493220b",
}

response = requests.post(url=exercise_endpoint, headers=headers, json=json_data)
response.raise_for_status()
data = response.json()

activities = []
durations = []
cals = []

for session in data["exercises"]:
    cals.append(round(session["nf_calories"]))
    activities.append((session["name"]))
    durations.append((session["duration_min"]))
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/d88706b86c623f6623e0c01c143266e2/workouts/workouts"
# iterate through the 3 lists
for (activity, duration, calories) in zip(activities, durations, cals):
    sheety_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": activity.title(),
            "duration": duration,
            "calories": calories
        }
    }

    headers = {
        "Authorization": os.environ.get("SHEETY_AUTH")      # from ENV Variables
    }
    add_row = requests.post(url=sheety_endpoint, json=sheety_input, headers=headers)
    add_row.raise_for_status()

print(requests.get(url=sheety_endpoint, headers=headers).json())
