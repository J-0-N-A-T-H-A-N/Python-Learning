import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pd.options.display.width = 0

df_tesla = pd.read_csv("data\TESLA Search Trend vs Price.csv")
df_daily_bitcoin = pd.read_csv("data\Daily Bitcoin Price.csv")
df_bitcoin_search = pd.read_csv("data\Bitcoin Search Trend.csv")
df_unemployment = pd.read_csv("data\\UE Benefits Search vs UE Rate 2004-19.csv")
df_unemployment_2 = pd.read_csv("data\\UE Benefits Search vs UE Rate 2004-20.csv")

print(f"Tesla Cols: {df_tesla.columns}")
print(f"Daily BC Cols: {df_daily_bitcoin.columns}")
print(f"BC Search Cols: {df_bitcoin_search.columns}")
print(f"UB Search Cols: {df_unemployment.columns}")
print(f"UB_2 Search Cols: {df_unemployment_2.columns}")

# print(df_tesla.columns, df_tesla.shape)
# print(df_daily_bitcoin.columns, df_daily_bitcoin.shape)
# print(df_bitcoin_search.columns, df_bitcoin_search.shape)
# print(df_unemployment.columns, df_unemployment.shape)
# print(df_unemployment_2.columns, df_unemployment_2.shape)
#

# # Find out if there are any NaN values
# print(df_tesla.isna().values.any())
# print(df_daily_bitcoin.isna().values.any())
# print(df_bitcoin_search.isna().values.any())
# print(df_unemployment.isna().values.any())
# print(df_unemployment_2.isna().values.any())
#
# # Find out how many Nan values
# print(f"Number of NaN values: {df_tesla.isna().values.sum()}")
# print(f"Number of NaN values: {df_daily_bitcoin.isna().values.sum()}")
# print(f"Number of NaN values: {df_bitcoin_search.isna().values.sum()}")
# print(f"Number of NaN values: {df_unemployment.isna().values.sum()}")
# print(f"Number of NaN values: {df_unemployment_2.isna().values.sum()}")

# Find the missing values
# print(df_daily_bitcoin[df_daily_bitcoin["CLOSE"].isna()])
# print(df_daily_bitcoin.shape)
# Drop the NaN row (2 values)
df_daily_bitcoin.dropna(inplace=True)      # using 'inplace' means don't need to use 'df_xx = df_xx.dropna()'
# print(df_daily_bitcoin.shape)

# Convert all the MONTH/DATE columns from str to panda timestamp
df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
df_daily_bitcoin["DATE"] = pd.to_datetime(df_daily_bitcoin["DATE"])
df_bitcoin_search["MONTH"] = pd.to_datetime(df_bitcoin_search["MONTH"])
df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])
df_unemployment_2["MONTH"] = pd.to_datetime(df_unemployment_2["MONTH"])

# print(df_daily_bitcoin.head())
# print(df_bitcoin_search.head())

# resample the daily bitcoin df to monthly using the last value of every month - could use also use e.g. mean()
df_monthly_bitcoin = df_daily_bitcoin.resample("M", on="DATE").last()

# print(f"\n Resampled: \n{df_monthly_bitcoin.head()}")
# print(df_monthly_bitcoin.shape, df_bitcoin_search.shape)

# print(df_tesla)
#
# ####### T E S L A   G R A P H
#
# plt.figure(figsize=(14, 8), dpi=100)         # Size the graph window
# plt.grid()
#
# plt.title("Tesla Web Search vs Price")
# plt.xticks(fontsize=14, rotation=45)            # Rotate the X-Axis ticks
#
# ax1 = plt.gca()                                 # Get Current Axis
# ax2 = ax1.twinx()
# # Set Y-Axis limits to maximum value + 10%
# ax1.set_ylim(0, (df_tesla["TSLA_USD_CLOSE"].max() * 1.1))
# ax2.set_ylim(0, (df_tesla["TSLA_WEB_SEARCH"].max() * 1.1))
#
# # Set Major and Minor Ticks on the x-axis for years & months
# years = mdates.YearLocator()
# years_fmt = mdates.DateFormatter("%Y")
# months = mdates.MonthLocator()
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel("Closing Price", color="lightcoral", fontsize=14)
# ax2.set_ylabel("Web Search", color="royalblue", fontsize=14)
#
# ax1.plot(df_tesla["MONTH"], df_tesla["TSLA_USD_CLOSE"], color="lightcoral", label="Closing Stock USD", linewidth=1.5)
# ax2.plot(df_tesla["MONTH"], df_tesla["TSLA_WEB_SEARCH"], color="royalblue", label="Web Search Popularity", linewidth=1.5)
#
# plt.show()

# ###
#       Bitcoin Data
# ###

# ####### B I T C O I N   G R A P H

# plt.figure(figsize=(14, 8), dpi=100)         # Size the graph window
# plt.grid()
#
# plt.title("Bitcoin News Search vs Resampled Price")
# plt.xticks(fontsize=14, rotation=45)            # Rotate the X-Axis ticks
#
# ax1 = plt.gca()                                 # Get Current Axis
# ax2 = ax1.twinx()
# # Set Y-Axis limits to maximum value + 10%
# ax1.set_ylim(0, (df_bitcoin_search["BTC_NEWS_SEARCH"].max() * 1.1))
# ax2.set_ylim(0, (df_monthly_bitcoin["CLOSE"].max() * 1.1))
#
# ax1.set_xlim(df_monthly_bitcoin.index.min(), df_monthly_bitcoin.index.max())
#
# # Set Major and Minor Ticks on the x-axis for years & months
# years = mdates.YearLocator()
# years_fmt = mdates.DateFormatter("%Y")
# months = mdates.MonthLocator()
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel("Bitcoin News Search", color="lightcoral", fontsize=14)
# ax2.set_ylabel("Sampled Closing Price USD", color="royalblue", fontsize=14)
#
# ax1.plot(df_monthly_bitcoin.index, df_bitcoin_search["BTC_NEWS_SEARCH"], color="lightcoral", linewidth=1.5, marker="o")
# ax2.plot(df_monthly_bitcoin.index, df_monthly_bitcoin["CLOSE"], color="royalblue", linewidth=1.5, linestyle="dashed", marker="o")
#
# print(df_monthly_bitcoin.columns)
#
# print(df_monthly_bitcoin.loc[df_monthly_bitcoin["CLOSE"].idxmax()])
# print(df_bitcoin_search.loc[df_bitcoin_search["BTC_NEWS_SEARCH"].idxmax()])
#
# plt.show()

####### U N E M P L O Y M E N T   G R A P H

# plt.figure(figsize=(14, 8), dpi=100)         # Size the graph window
#
# plt.title("Unemployment Benefits in the U.S. vs the U/E Rate")
# plt.xticks(fontsize=14, rotation=45)            # Rotate the X-Axis ticks
#
# ax1 = plt.gca()                                 # Get Current Axis
# ax2 = ax1.twinx()
# ax1.grid(color="lightgrey", linestyle="dashed")
# # Set Y-Axis limits to maximum value + 10%
# ax1.set_ylim(0, (df_unemployment["UE_BENEFITS_WEB_SEARCH"].max() * 1.1))
# ax2.set_ylim(0, (df_unemployment["UNRATE"].max() * 1.1))
#
# ax1.set_xlim(df_unemployment["MONTH"].min(), df_unemployment["MONTH"].max())
#
# # Set Major and Minor Ticks on the x-axis for years & months
# years = mdates.YearLocator()
# years_fmt = mdates.DateFormatter("%Y")
# months = mdates.MonthLocator()
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel("Benefits Web Search", color="lightcoral", fontsize=14)
# ax2.set_ylabel("Unemployment Rate", color="royalblue", fontsize=14)
#
# ax1.plot(df_unemployment["MONTH"], df_unemployment["UE_BENEFITS_WEB_SEARCH"], color="lightcoral", linewidth=1.5)
# ax2.plot(df_unemployment["MONTH"], df_unemployment["UNRATE"], color="royalblue", linewidth=1.5, linestyle="dashed")
#
# plt.show()



####### U N E M P L O Y M E N T   G R A P H
#
# rolling_df = df_unemployment[["UE_BENEFITS_WEB_SEARCH", "UNRATE"]].rolling(window=6).mean()
# print(rolling_df.columns)
#
#
# plt.figure(figsize=(14, 8), dpi=100)         # Size the graph window
#
# plt.title("Unemployment Benefits in the U.S. vs the U/E Rate")
# plt.xticks(fontsize=14, rotation=45)            # Rotate the X-Axis ticks
#
# ax1 = plt.gca()                                 # Get Current Axis
# ax2 = ax1.twinx()
# ax1.grid(color="lightgrey", linestyle="dashed")
# # Set Y-Axis limits to maximum value + 10%
# ax1.set_ylim(0, (rolling_df["UE_BENEFITS_WEB_SEARCH"].max() * 1.1))
# ax2.set_ylim(0, (rolling_df["UNRATE"].max() * 1.1))
#
# ax1.set_xlim(df_unemployment["MONTH"].min(), df_unemployment["MONTH"].max())
#
# # Set Major and Minor Ticks on the x-axis for years & months
# years = mdates.YearLocator()
# years_fmt = mdates.DateFormatter("%Y")
# months = mdates.MonthLocator()
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel("Benefits Web Search", color="lightcoral", fontsize=14)
# ax2.set_ylabel("Unemployment Rate", color="royalblue", fontsize=14)
#
# ax1.plot(df_unemployment["MONTH"], rolling_df["UE_BENEFITS_WEB_SEARCH"], color="lightcoral", linewidth=1.5)
# ax2.plot(df_unemployment["MONTH"], rolling_df["UNRATE"], color="royalblue", linewidth=1.5, linestyle="dashed")
#
# plt.show()



####### U N E M P L O Y M E N T 2  G R A P H

plt.figure(figsize=(14, 8), dpi=100)         # Size the graph window

plt.title("Unemployment Benefits in the U.S. vs the U/E Rate")
plt.xticks(fontsize=14, rotation=45)            # Rotate the X-Axis ticks

ax1 = plt.gca()                                 # Get Current Axis
ax2 = ax1.twinx()
ax1.grid(color="lightgrey", linestyle="dashed")
# Set Y-Axis limits to maximum value + 10%
ax1.set_ylim(0, (df_unemployment_2["UE_BENEFITS_WEB_SEARCH"].max() * 1.1))
ax2.set_ylim(0, (df_unemployment_2["UNRATE"].max() * 1.1))

ax1.set_xlim(df_unemployment_2["MONTH"].min(), df_unemployment_2["MONTH"].max())

# Set Major and Minor Ticks on the x-axis for years & months
years = mdates.YearLocator()
years_fmt = mdates.DateFormatter("%Y")
months = mdates.MonthLocator()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel("Benefits Web Search", color="lightcoral", fontsize=14)
ax2.set_ylabel("Unemployment Rate", color="royalblue", fontsize=14)

ax1.plot(df_unemployment_2["MONTH"], df_unemployment_2["UE_BENEFITS_WEB_SEARCH"], color="lightcoral", linewidth=1.5)
ax2.plot(df_unemployment_2["MONTH"], df_unemployment_2["UNRATE"], color="royalblue", linewidth=1.5, linestyle="dashed")

plt.show()

