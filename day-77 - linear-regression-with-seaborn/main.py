import pandas as pd

pd.options.display.width = 0
raw_df = pd.read_csv("cost_revenue_dirty.csv")

print(f"The DataFrame has {raw_df.shape[0]} rows & {raw_df.shape[1]} columns")

# print(f"\nNaN Values: \n")
# print(raw_df.isna().values.any())
# print(f"\nDuplicated Values: \n")
# print(raw_df.duplicated().values.any())
# print(f"\nDF Info: \n")
# print(raw_df.info())


raw_df["USD_Production_Budget"] = raw_df["USD_Production_Budget"].replace('\$', '', regex=True)
raw_df["USD_Production_Budget"] = raw_df["USD_Production_Budget"].replace(',', '', regex=True)
raw_df["USD_Production_Budget"] = pd.to_numeric(raw_df["USD_Production_Budget"])

raw_df["USD_Worldwide_Gross"] = raw_df["USD_Worldwide_Gross"].replace('\$', '', regex=True)
raw_df["USD_Worldwide_Gross"] = raw_df["USD_Worldwide_Gross"].replace(',', '', regex=True)
raw_df["USD_Worldwide_Gross"] = pd.to_numeric(raw_df["USD_Worldwide_Gross"])

raw_df["USD_Domestic_Gross"] = raw_df["USD_Domestic_Gross"].replace('\$', '', regex=True)
raw_df["USD_Domestic_Gross"] = raw_df["USD_Domestic_Gross"].replace(',', '', regex=True)
raw_df["USD_Domestic_Gross"] = pd.to_numeric(raw_df["USD_Domestic_Gross"])

raw_df["Release_Date"] = pd.to_datetime(raw_df["Release_Date"])

# print(raw_df[raw_df["USD_Domestic_Gross"] == 0])

print(raw_df[["Movie_Title", "USD_Production_Budget"]].loc[raw_df["USD_Production_Budget"].idxmax()])
print(f"\nAverage Production Budget: {raw_df['USD_Production_Budget'].mean()}")
print(f"\nAverage Worldwide Gross: {raw_df['USD_Worldwide_Gross'].mean()}")
print(f"\nLowest Worldwide Gross: {raw_df['USD_Worldwide_Gross'].min()}")
print(f"\nLowest Domestic Gross: {raw_df['USD_Domestic_Gross'].min()}")
print(f"\nHighest Worldwide Gross: {raw_df['USD_Worldwide_Gross'].max()}")

print(f"\nHighest budget movie:\n "
      f"{raw_df[['USD_Worldwide_Gross', 'Movie_Title']].loc[raw_df['USD_Production_Budget'].idxmax()]}")
print(f"\nLowest budget movie:\n "
      f"{raw_df[['USD_Worldwide_Gross', 'Movie_Title']].loc[raw_df['USD_Production_Budget'].idxmin()]}")

print(raw_df[raw_df["USD_Domestic_Gross"] == 0].sort_values(by="USD_Production_Budget", ascending=False).head())
print(raw_df[raw_df["USD_Domestic_Gross"] == 0].count())

print(raw_df[raw_df["USD_Worldwide_Gross"] > 0].sort_values(by="USD_Production_Budget", ascending=False).head())

# Worldwide Gross is less than the budget

profit = raw_df["USD_Worldwide_Gross"] - raw_df["USD_Production_Budget"]
raw_df.insert(6, "Profit", profit)

print(raw_df[raw_df["USD_Worldwide_Gross"] < raw_df["USD_Production_Budget"]].sort_values(by="Profit", ascending=True).head())