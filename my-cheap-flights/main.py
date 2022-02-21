import pandas
from flight_manager import FlightManager
from organise_results import Organiser


HOME_AIRPORT = "ORK"        # ORK, DUB, BFS (Antrim), BHD (Belfast City)

flight_file = "data\\flights.csv"
flight_mgr = FlightManager()

flight_data = pandas.read_csv(flight_file)
update_flight_file = False
for index, city in flight_data.iterrows():
    nullcode = pandas.isnull(city["iatacode"])
    if nullcode:
        update_flight_file = True
        city_code = flight_mgr.update_codes(city["city"])
        flight_data.loc[index, "iatacode"] = city_code

if update_flight_file:
    df = pandas.DataFrame(flight_data)
    df.to_csv("data/flights.csv", index=False)

new_search = flight_mgr.search_flights(HOME_AIRPORT, flight_data)

display_results = Organiser(new_search)
