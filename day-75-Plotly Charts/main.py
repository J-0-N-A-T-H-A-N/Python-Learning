import pandas as pd
import plotly.express as px

pd.options.display.width = 0
df_apps = pd.read_csv("apps.csv")

# print(f"Shape: {df_apps.shape}")
# print(f"Columns: {df_apps.columns}")
# # Random sample of rows
# print(df_apps.sample(n=5))
#

# print(df_apps.columns)
df_apps.drop(axis=1, inplace=True, columns=["Last_Updated", "Android_Ver"])
# print(df_apps.columns)

# Print total number of  Nan Values
# print(f"Total Number of NaN Values: {df_apps.isna().values.sum()}")
# Print NaN values
# print(df_apps[df_apps.isna()])

# Create new df without the NaN values
df_apps_clean = df_apps.dropna()
# print(df_apps_clean.shape)
#
# print(df_apps_clean[df_apps_clean["App"] == "Instagram"])
# print(f"Duplicates: {df_apps_clean[df_apps_clean.duplicated()]}")
# print(df_apps_clean.shape)
# Clean out duplicates, giving columns to use for comparison - if these match, considered duplicate.
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
# print(df_apps_clean.shape)

# print(df_apps_clean[df_apps_clean["App"] == "Instagram"])
# # Print all the unique entries in the Category Column
# print(df_apps_clean["Category"].unique())
#
# # List all top rated apps
# print(df_apps_clean[df_apps_clean["Rating"] == df_apps_clean["Rating"].max()].sort_values(by="Reviews", ascending=False))
# # List all the biggest apps
# print(df_apps_clean[df_apps_clean["Size_MBs"] == df_apps_clean["Size_MBs"].max()])
# # List the highest number of reviews
# print(df_apps_clean[df_apps_clean["Reviews"] == df_apps_clean["Reviews"].max()])
#
# print(df_apps_clean.sort_values(by="Reviews", ascending=False).head(50))


ratings = df_apps_clean["Content_Rating"].value_counts()
# print(ratings)
#   Print a PlotLy Pie Chart
# fig = px.pie(labels=ratings.index, values=ratings.values, title="App Content Ratings", names=ratings.index, hole=0.5)
# fig.update_traces(textposition='outside', textinfo='percent+label')
#
#
# fig.show()

# columns = df_apps_clean.columns
# for col in columns:
#     print(f"{col} type: {type(df_apps_clean[col].iloc[0])}")

# Remove commas from the string field
df_apps_clean["Installs"] = df_apps_clean["Installs"].replace(",", "", regex=True)
# Convert string to a number
df_apps_clean["Installs"] = pd.to_numeric(df_apps_clean["Installs"])


# print(df_apps_clean[df_apps_clean["Installs"] >= 1000000000])
#
# print(df_apps_clean[["App", "Installs"]].groupby(by="Installs").count())
#
# # # Get info on the df
# # df_apps_clean.info()
#
# print(df_apps_clean[df_apps_clean["Installs"] == 1])

df_apps_clean["Price"] = df_apps_clean["Price"].replace('\$', '', regex=True)

df_apps_clean["Price"] = pd.to_numeric(df_apps_clean["Price"])

# print(df_apps_clean[["App", "Price"]].sort_values(by="Price", ascending=False).head(20))

# print(df_apps_clean[["App", "Price", "Installs"]][df_apps_clean["Price"] > 250].sort_values(by="Price", ascending=False))
# print(df_apps_clean.shape)
# Drop rows where price > 250
df_apps_clean.drop(df_apps_clean[df_apps_clean["Price"] > 250].index, inplace=True)
# print(df_apps_clean.shape)

est_revenue = df_apps_clean["Installs"] * df_apps_clean["Price"]
df_apps_clean.insert(10, "Revenue_Estimate", est_revenue)

# print(df_apps_clean.sort_values("Revenue_Estimate", ascending=False).head(10))
# print(df_apps_clean.groupby(by="Category").sum().sort_values(by="Installs", ascending=False))

# Apps per category - sliced for top-20
apps_per_category = df_apps_clean["Category"].value_counts()[:20]

# bar_chart = px.bar(x=apps_per_category.index, y=apps_per_category.values, title="Apps per Category")
# bar_chart.show()

category_app_count = df_apps_clean.groupby(by="Category").agg({"App": pd.Series.count})
# print(category_app_count)
category_install_count = df_apps_clean.groupby(by="Category").agg({"Installs": pd.Series.sum})
# print(category_install_count)

df_merged = pd.merge(category_app_count, category_install_count, on="Category")
# print(df_merged)

# Print scatter graph for concentration of apps in each category
# scatter = px.scatter(df_merged,
#                      x="App",
#                      y="Installs",
#                      color='Installs',
#                      size='App',
#                      title="Category Concentration",
#                      hover_name=df_merged.index)
# scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
#                       yaxis_title="Installs",
#                       yaxis=dict(type='log'))
#
# scatter.show()

# print(df_apps_clean["Genres"].unique())

# print(f"Count: {df_apps_clean['Genres'].count().sort_values(ascending=False)}")
# print(f"Value Counts:\n{df_apps_clean['Genres'].value_counts().tail()}")

# For Apps with multiple Genres, split them and create a new list with individual Genres.
stack = df_apps_clean['Genres'].str.split(";", expand=True).stack()
# print(stack.count())
num_genres = stack.value_counts()
# print(f"Number of Genres: {len(num_genres)}")
#
# bar = px.bar(x=num_genres.index[:15],
#              y=num_genres.values[:15],
#              title="Top 15 Genres",
#              color=num_genres.values[:15],
#              color_continuous_scale="Agsunset"
#              )
# bar.update_layout(xaxis_title='Genre',yaxis_title='Number of Apps',coloraxis_showscale=False)
#
# bar.show()

print(df_apps_clean["Type"].value_counts())

# Group by Category and then by Type
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({"App": pd.Series.count})
# print(df_free_vs_paid.shape)
# print(df_free_vs_paid.info())
#
# bar = px.bar(df_free_vs_paid,
#              x="Category",
#              y="App",
#              color="Type",
#              barmode="group")
#
# # Change the display order and a log scale
# bar.update_xaxes(categoryorder="total descending")
# bar.update_layout(yaxis=dict(type="log"))
# bar.show()

# Box Plot
df_paid_apps = df_apps_clean[df_apps_clean["Type"] == "Paid"]
box = px.box(df_paid_apps,
             x="Category",
             y="Revenue_Estimate",
             title="How Many Downloads are Paid Apps Giving Up?"
             )
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder':'min ascending'},
                  yaxis=dict(type='log'))
box.show()

