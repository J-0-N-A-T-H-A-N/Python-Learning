import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.from_ = "ORK"
        self.to_ = "CDG"
        self.tequila_api_key = "vrRbVbDYwvqoQeQPwcO__Urg0Y23HFyy"
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.search_params = {
            "fly_from": self.from_,
            "fly_to": self.to_,
            "date_from": "01/03/2022",
            "date_to": "01/06/2022",
            "one_for_city": 0,
            # "select_airlines": "FR,EI",
            "nights_in_dst_from": 4,
            "nights_in_dst_to": 7,
        }
        self.header = {
            "apikey": self.tequila_api_key
        }
        response = requests.get(url=self.tequila_endpoint, params=self.search_params, headers=self.header)
        response.raise_for_status()
        self.search_data = response.json()
        # print(self.search_data)


