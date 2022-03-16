import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.options.display.width = 0        # Allows PyCharm to display all columns
pd.options.display.float_format = '{:,.2f}'.format  # Format numbers to 2 decimal points

data_df = pd.read_csv("nobel_prize_data.csv")
print(data_df.shape)
print("NaN Values:")
print(data_df.isna().sum())
print("Duplicates:")
print(data_df.duplicated().sum())

print(data_df.columns)
print(f"Earliest: {data_df['year'].min()}")
print(f"Latest: {data_df['year'].max()}")

col_subset = ['year','category', 'laureate_type',
              'birth_date','full_name', 'organization_name']
# Print rows where birth_date is NaN
print(data_df.loc[data_df.birth_date.isna()][col_subset])
# Print rows where organization_name is Nan
print(data_df.loc[data_df["organization_name"].isna()][col_subset])

# Convert the DOB to pandas Date format
data_df["birth_date"] = pd.to_datetime(data_df["birth_date"])

split_fraction = data_df["prize_share"].str.split("/", expand=True)
numerator = pd.to_numeric(split_fraction[0])
denominator = pd.to_numeric(split_fraction[1])
share_pct = numerator / denominator * 100
data_df.insert(16, "share_pct", share_pct)

print(data_df.sample(10))
print(data_df.info())

# # Donut chart of male/female split
# labels = ["Male", "Female"]
# values = [data_df["sex"][data_df["sex"] == "Male"].count(), data_df["sex"][data_df["sex"] == "Female"].count()]
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
# fig.show()

print(data_df[data_df["sex"] == "Female"].head(3))

# Did anyone ever get the nobel prize more than once?
print(f"\nDid anyone ever get the nobel prize more than once?")
print(data_df[["full_name", "category", "year", "motivation"]][data_df["full_name"].duplicated(keep=False)].sort_values("full_name"))
print(f"\n")
print(data_df["category"].nunique())
print(data_df["category"].value_counts())

# fig = go.Figure(data=go.Bar(y=data_df["category"][data_df["year"] >= 2000].value_counts(), x=data_df["category"][data_df["year"] >= 2000].value_counts().index),
#                 layout_title_text="Nobel Prize by Category since 2000")
# fig2 = go.Figure(data=go.Bar(y=data_df["category"].value_counts(), x=data_df["category"].value_counts().index),
#                 layout_title_text="Nobel Prize by Category - all time")
# fig.show()
# fig2.show()
#

# print(data_df[["category", "year", "full_name"]][data_df["category"] == "Economics"].head())

cat_men_women = data_df.groupby(['category', 'sex'], as_index=False).agg({'prize': pd.Series.count})
# In-place sort
cat_men_women.sort_values('prize', ascending=False, inplace=True)
print(cat_men_women)

v_bar_split = px.bar(x=cat_men_women["category"],
                     y=cat_men_women["prize"],
                     color=cat_men_women["sex"],
                     title='Number of Prizes Awarded per Category split by Men and Women')

v_bar_split.update_layout(xaxis_title='Nobel Prize Category',
                          yaxis_title='Number of Prizes')
v_bar_split.show()
