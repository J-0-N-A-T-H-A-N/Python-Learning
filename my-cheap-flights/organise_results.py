import pandas


class Organiser():
    def __init__(self, results):
        self.results = results
        max_flights = 2         # 2 indicates 1 each way (direct)
        price_list = []
        airline_list = []
        dep_date_list = []
        dep_time_list = []
        ret_date_list = []
        ret_time_list = []
        dest_list = []

        for flight in results["data"]:
            destination = flight["flyTo"]
            price = flight["price"]
            airlines = flight["airlines"]
            routes = len(flight["route"])
            departure = flight["local_departure"].split("T")
            dep_date = departure[0]
            dep_time = departure[1].split(".")[0]
            if routes <= max_flights:
                return_datetime = flight["route"][-1]["local_departure"].split("T")
                ret_date = return_datetime[0]
                ret_time = return_datetime[1].split(".")[0]
                #print(f"{destination}: {airlines}: {routes}: {dep_date}: {dep_time}: {ret_date}: {ret_time}: {price}")
                price_list.append(price)
                dest_list.append(destination)
                airline_list.append(airlines)
                dep_date_list.append(dep_date)
                dep_time_list.append(dep_time)
                ret_date_list.append(ret_date)
                ret_time_list.append(ret_time)

        data = {
            "Dest Airport": dest_list,
            "Airline(s)": airline_list,
            "Dep Date": dep_date_list,
            "Dep Time": dep_time_list,
            "Ret Date": ret_date_list,
            "Ret Time": ret_time_list,
            "Price": price_list,
        }
        df = pandas.DataFrame(data)
        print(df.to_string(index=False))
