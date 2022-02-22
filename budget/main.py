import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

HOUSE_VALUE = 450000

pd.options.display.width = 0
df = pd.read_csv("datafile.csv", index_col=0)   # Make Date the Index

# Drop full rows and columns of NaN
clean_df = df.dropna(axis=0, how="all")
clean_df = clean_df.dropna(axis=1, how="all")

# Replace remaining NaN with zero
clean_df.fillna(0, inplace=True)

# Make the DATE string a datatime datatype
clean_df.index = pd.to_datetime(clean_df.index)  # Change index from str to datetime data type

# Select only dates less than today
now = dt.datetime.now().strftime("%Y-%m-%d")
clean_df = clean_df[clean_df.index < now]
total_credit = clean_df["JG AIB LOAN"] + clean_df["AG AIB LOAN"] + clean_df["Chill Visa"] + clean_df["AG AIB VISA"]
clean_df.insert(6, "Total Credit", total_credit)
grand_total = clean_df["Mortgage"] + clean_df["Total Credit"]
clean_df.insert(7, "Grand Total", grand_total)
net_worth = HOUSE_VALUE - clean_df["Grand Total"] + clean_df["SAVINGS"]
clean_df.insert(8, "Net Worth", net_worth)

print(clean_df.tail())
#
# print(clean_df[["Mortgage", "SAVINGS"]])

plt.figure(figsize=(16, 10))
plt.ylim(0, 350000)

plt.plot(clean_df.index, clean_df[["Mortgage","Total Credit", "SAVINGS", "Net Worth"]].values)
plt.legend(["MORTGAGE","TOTAL CREDIT", "SAVINGS", "NET WORTH"])
plt.grid(visible=True, which="major", axis="both")
plt.savefig("graph.png", format="png")      # This will overwrite every run
# plt.show()



