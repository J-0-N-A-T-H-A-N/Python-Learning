import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = 0
# Read CSV and add column names - header=0 allows to add own column names without assuming row 1 contains names
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# print(df)
#
# # Print first and last 5 rows
# print(df.head())
# print(df.tail())
#
# # Number of posts per Tag
# print(f"Posts per Tag:\n {df.groupby('TAG').sum()}\n====================")
# # Number of entries per Tag
# print(f"Entries per Tag:\n {df.groupby('TAG').count()}\n===========================")

# Convert data str entry to a time data type
# print(df["DATE"][1])
# print(type(df["DATE"][1]))
#
df["DATE"] = pd.to_datetime(df["DATE"])
# print(df["DATE"][1])
# print(type(df["DATE"][1]))
#
# print(df)


pivoted_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
# Replace NaN entries with zeros
pivoted_df.fillna(0, inplace=True)
# print(pivoted_df)
# print(pivoted_df.columns)
# print(f"Pivot shape: {pivoted_df.shape}")
# print(f"Original shape: {df.shape}")
# print(pivoted_df.count())

# Check for any NaN values in the pivoted table
# print(pivoted_df.isna().values.any())

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Post", fontsize=14)
plt.ylim(0,35000)
#
# java_data = pivoted_df["java"]
# python_data = pivoted_df["python"]
# # plt.plot(pivoted_df.index, java_data)
# # plt.plot(pivoted_df.index, python_data)
# # Use all data from pivoted_df
# plt.plot(pivoted_df.index, pivoted_df.values)
# plt.legend(pivoted_df.columns, fontsize=12)         # Has to be after the data entry
#
# plt.title("Posts per month")
# plt.show()

## Smoothing out time series

roll_df = pivoted_df.rolling(window=12).mean()
roll_df.fillna(0, inplace=True)

# print(roll_df)

# plt.plot(roll_df.index, roll_df.values)
# plt.legend(roll_df.columns, fontsize=12)         # Has to be after the data entry
#
# plt.title("Posts per month")
# plt.show()


# print(result)
# Display data before 2013
# post_per_language = df[df["DATE"] < "2013"].groupby("TAG").sum()
# print(post_per_language)

# Display data between the from 2015 to 2018
# post_per_language = df[(df["DATE"] <= "2017") & (df["DATE"] >= "2015")].groupby("TAG").sum()
# print(post_per_language)

# Display data for just 2020
# post_per_language = df[df["DATE"] == "2020"].groupby("TAG").sum()
# print(post_per_language)
