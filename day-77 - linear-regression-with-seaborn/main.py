import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

international_releases = raw_df.loc[(raw_df["USD_Domestic_Gross"] == 0) & (raw_df["USD_Worldwide_Gross"] != 0)].sort_values(by="Profit", ascending=False).head()
print("International Only:")
print(international_releases)

international_query = raw_df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print("International Query:")
print(international_query)
print(len(international_query))

zero_revenue = raw_df.query('Release_Date > "2018-05-01"')
print("Released after data gathering:")
print(zero_revenue)
print(len(raw_df))
# Remove un-released movies from the raw_df df and create data_clean
data_clean = raw_df.drop(zero_revenue.index)
print(len(data_clean))

loss_makers = data_clean.query('Profit < 0')
print("Money Losers:")
print(loss_makers)
percentage_losers = len(loss_makers) / len(data_clean) * 100
print(f"Percentage of films that lost money: {percentage_losers:.2f}%")

# plt.figure(figsize=(8, 4), dpi=200)
# # set styling on a single chart
# with sns.axes_style('darkgrid'):
#       ax = sns.scatterplot(data=data_clean,
#                            x='USD_Production_Budget',
#                            y='USD_Worldwide_Gross',
#                            hue='USD_Worldwide_Gross',
#                            size='USD_Worldwide_Gross')
#
#       ax.set(ylim=(0, 3000000000),
#              xlim=(0, 450000000),
#              ylabel='Revenue in $ billions',
#              xlabel='Budget in $100 millions')
#
# plt.figure(figsize=(8, 4), dpi=200)
#
# with sns.axes_style("whitegrid"):
#       ax = sns.scatterplot(data=data_clean,
#                            x='Release_Date',
#                            y='USD_Production_Budget',
#                            hue='USD_Worldwide_Gross',
#                            size='USD_Worldwide_Gross', )
#
#       ax.set(ylim=(0, 450000000),
#              xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
#              xlabel='Year',
#              ylabel='Budget in $100 millions')
# plt.show()

data_clean.info()
release_year = pd.DatetimeIndex(data_clean["Release_Date"]).year
decade = release_year // 10     # Floor division
data_clean.insert(7, "Decade", decade * 10)
print(data_clean.head())

old_films = data_clean.query('Decade < 1970')
new_films = data_clean.query('Decade >= 1970')

print(f"Pre 1970 movies: {len(old_films)}")
print(f"Post 1970 movies: {len(new_films)}")

print(f"Most expensive movie pre-1970: {old_films[['Movie_Title', 'USD_Production_Budget']].loc[old_films['USD_Production_Budget'].idxmax()]}")
print(f"Least expensive movie post-1970: {new_films[['Movie_Title', 'USD_Production_Budget']].loc[new_films['USD_Production_Budget'].idxmin()]}")

print(f"Highest Revenue movie pre-1970: {old_films[['Movie_Title', 'USD_Worldwide_Gross']].loc[old_films['USD_Worldwide_Gross'].idxmax()]}")

# plt.figure(figsize=(8,4), dpi=200)        # This creates the first plot
# with sns.axes_style("whitegrid"):
#     ax = sns.regplot(data=old_films,
#                 x='USD_Production_Budget',
#                 y='USD_Worldwide_Gross',
#                 scatter_kws={'alpha': 0.4},
#                 line_kws={'color': 'black'})
#     ax.set(xlabel='Old Films')
plt.figure(figsize=(8,4), dpi=200)        # This creates the second plot
with sns.axes_style("darkgrid"):
    ax = sns.regplot(data=new_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'blue'})
    ax.set(xlabel='New Films')

plt.show()        # Show both plots

# SciKit Regression
regression = LinearRegression()

# Explanatory Variable(s) or feature(s)
X = pd.DataFrame(new_films, columns=["USD_Production_Budget"])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=["USD_Worldwide_Gross"])

regression.fit(X, y)
print(regression.intercept_)
print(regression.coef_)

# R-Squared
print(regression.score(X, y))

budget = 350000000
est_revenue = float(budget * regression.coef_[0] + regression.intercept_[0])
print(f"The estimated revenue for a movie budget of ${budget / 1000000}M is ${est_revenue / 1000000:.0f}M")

# # # Switch to old_films
# # Explanatory Variable(s) or feature(s)
# X = pd.DataFrame(old_films, columns=["USD_Production_Budget"])
#
# # Response Variable or Target
# y = pd.DataFrame(old_films, columns=["USD_Worldwide_Gross"])
#
# regression.fit(X, y)
# print(regression.intercept_)
# print(regression.coef_)
#
# # R-Squared
# print(regression.score(X, y))