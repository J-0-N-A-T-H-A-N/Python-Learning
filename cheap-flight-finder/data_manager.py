import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/d88706b86c623f6623e0c01c143266e2/flights/prices"
        self.sheety_data = requests.get(url=self.sheety_endpoint).json()
        self.auth_key = "Bearer piyhkdhtBDJEY789!!lTTs"

    def update_codes(self):
        for entry in self.sheety_data["prices"]:
            city = entry["city"]
            city_id = entry["id"]

            tequila_api_key = "vrRbVbDYwvqoQeQPwcO__Urg0Y23HFyy"
            tequila_endpoint = "https://tequila-api.kiwi.com/locations/query"
            params = {
                "term": city
            }
            header = {
                "apikey": tequila_api_key,
                "location_types": "airport"
            }

            tequila_data = requests.get(url=tequila_endpoint, params=params, headers=header)
            tequila_data.raise_for_status()
            city_code = tequila_data.json()["locations"][0]["code"]

            sheety_row_data = {
                "price": {
                    "iataCode": city_code,
                }
            }
            header = {
                "Authorization": self.auth_key
            }
            update_endpoint = f"{self.sheety_endpoint}/{city_id}"
            update_sheety = requests.put(url=update_endpoint, json=sheety_row_data, headers=header)
            update_sheety.raise_for_status()
            self.sheety_data = requests.get(url=self.sheety_endpoint).json()
