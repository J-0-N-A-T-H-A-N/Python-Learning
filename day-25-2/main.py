import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# colours = data["Primary Fur Color"]
# result = colours.value_counts()
# result.to_csv("colour_count.csv")
#
# colour = pandas.read_csv("colour_count.csv")
# colour.
# print(colour)

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(gray, red, black)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

colour_dataframe = pandas.DataFrame(data_dict)
colour_dataframe.to_csv("colours.csv")

print(colour_dataframe)