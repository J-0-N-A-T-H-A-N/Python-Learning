import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
headings = data.columns.values

print(headings)

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

fur_dict = {
    "Fur Colour": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(fur_dict)
# df.to_csv("Fur_Colour.csv")

#Save series (column) to a list
data = data["Other Activities"].tolist()
for item in data:
    print(item)