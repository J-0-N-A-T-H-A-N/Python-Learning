
import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
#
# print(f'Mean of series: {data["temp"].mean():.2f}C')
# print(f'Maximum of series: {data["temp"].max()}C')
#
# print(data.condition)

# result = data[data["temp"] == data["temp"].max()]
# print(result)
# print(type(result))

# monday = data[data["day"] == "Monday"]
# temp_in_C = int(monday.temp)
# temp_in_F = (temp_in_C * (9 / 5)) + 32
# print(f"{temp_in_C}C is {temp_in_F}F")

#Create dataframe
data_dict = {
    "students": ["Dave", "Joan", "Amy"],
    "scores": [88, 89, 73]
}
scores = pandas.DataFrame(data_dict)
scores.to_csv("scores.csv")
print(scores)
