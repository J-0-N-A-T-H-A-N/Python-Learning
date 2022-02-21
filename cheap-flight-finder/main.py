#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()
sheet_data = sheety.sheety_data
needs_iatacode_update = False

# for city in sheet_data["prices"]:
#     if city["iataCode"] == "":
#         needs_iatacode_update = True
#
# if needs_iatacode_update:
#     print("Updating IATA Codes....")
#     sheety.update_codes()
#     sheet_data = sheety.sheety_data

new_search = FlightSearch()
data = new_search.search_data
print(data)
currency = data["currency"]
for flight in data["data"]:
    price = flight["price"]
    airline = flight["airlines"]
    fly_to_airport = flight["flyTo"]
    nights = flight["nightsInDest"]
    depart = flight["local_departure"]
    print(f"{airline}: {fly_to_airport}: {nights} nights from {depart} {price} ({currency})")
    # print(data["route"])


