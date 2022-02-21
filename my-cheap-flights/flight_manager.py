import requests


class FlightManager:

    def __init__(self):
        self.id = 1
        self.tequila_api_key = "vrRbVbDYwvqoQeQPwcO__Urg0Y23HFyy"


    def update_codes(self, city):
        tequila_endpoint = "https://tequila-api.kiwi.com/locations/query"
        params = {
            "term": city
        }
        header = {
            "apikey": self.tequila_api_key,
            "location_types": "airport"
        }

        tequila_data = requests.get(url=tequila_endpoint, params=params, headers=header)
        tequila_data.raise_for_status()
        city_code = tequila_data.json()["locations"][0]["code"]

        return city_code

    def search_flights(self, fly_from, flight_info):
        tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        fly_to = []
        for index, city in flight_info.iterrows():
            fly_to.append(city['iatacode'])
        fly_to_str = ",".join(fly_to)

        print(f"{fly_from} --> {fly_to_str}")
        search_params = {
            "fly_from": fly_from,
            "fly_to": fly_to_str,
            "date_from": "01/03/2022",
            "date_to": "01/10/2022",
            "one_for_city": 1,
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 7,
            #"limit": 20,
        }
        header = {
            "apikey": self.tequila_api_key
        }
        response = requests.get(url=tequila_endpoint, params=search_params, headers=header)
        # print(response.text)
        response.raise_for_status()

        search_data = response.json()
        return search_data
