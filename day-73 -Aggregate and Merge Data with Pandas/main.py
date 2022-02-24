import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# WORKING WITH COLORS.CSV
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# df = pd.read_csv("data/colors.csv")
#
#
# print(df.head())
# print(f"\n")
#
# # Display count of unique row for each columns
# print(df.nunique())
# print(f"\n")
# # Display count of unique row for "name"
# print(df["name"].nunique())
#
# # Three ways to get the number of 't' and 'f' for 'is_trans'
# # 1
# print(f"\nTransparent: {df['is_trans'][df['is_trans'] == 't'].count()}")
# print(f"Non Transparent: {df['is_trans'][df['is_trans'] == 'f'].count()}\n")
# # 2
# print(df.groupby("is_trans").count())
# print(f"\n")
# # 3
# print(df["is_trans"].value_counts())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# WORKING WITH SETS.CSV
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
sets_df = pd.read_csv("data/sets.csv")

# # print(sets_df.head())
#
# print(sets_df[["name", "num_parts"]].loc[sets_df["num_parts"].idxmax()])
# print(f"\n")
# print(sets_df[["name", "num_parts"]].loc[sets_df["num_parts"].idxmin()])
#
# # Display sets release earliest
# earliest_year = sets_df["year"].min()
# print(sets_df[["name", "year"]][sets_df["year"] == earliest_year])
# print(f"\nNumber of sets produced in {earliest_year}: {sets_df['name'][sets_df['year'] == earliest_year].count()}\n")
#
# # The top 5 LEGO sets with the most number of parts
# print(sets_df.sort_values(by="num_parts", ascending=False).head())
# print(f"\n")
# # The top 5 LEGO sets with the least number of parts
# print(sets_df.sort_values(by="num_parts", ascending=True).head())
# print(f"\n")
#
# # Number of sets by year
# print(sets_df.groupby("year").count().sort_values(by="name", ascending=False).head())
# print(sets_df.groupby("year").count().sort_values(by="name", ascending=True).head())
#
# sets_per_year = sets_df.groupby("year").count()["set_num"]
#
# # Plot with last 2 years sliced off
#
#
# print(sets_df.columns)
#
# grouped_by_year = sets_df.groupby("year")
# themes_by_year = grouped_by_year["theme_id"].nunique()
# print(themes_by_year[:-1])
#
# # Use  .agg() function to do the same as above
# themes_per_year = sets_df.groupby("year").agg({"theme_id": pd.Series.nunique})
# # Change column to reflect better the values
# themes_per_year.rename(columns={"theme_id": "Unique Themes"}, inplace=True)
#
# # ###### Plot 2 lines, with 2 different Y-axes
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(sets_per_year.index[:-2], sets_per_year[:-2], color="blue")
# ax2.plot(themes_per_year.index[:-2], themes_per_year["Unique Themes"][:-2], color="orange")
#
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of Sets", color="blue")
# ax2.set_ylabel("Number of Unique Themes", color="orange")
#
# plt.show()


# parts_per_set = sets_df.groupby("year").agg({"num_parts": pd.Series.mean})
# print(parts_per_set.head())
#
# plt.plot(parts_per_set.index[:-2], parts_per_set["num_parts"][:-2])
# plt.scatter(parts_per_set.index[:-2], parts_per_set["num_parts"][:-2], c="orange")
# plt.show()


sets_per_theme = sets_df["theme_id"].value_counts()             # This creates a panda series
print(type(sets_per_theme))
# Convert to a Dataframe and ensure it has a 'id' column as the themes df does below
sets_per_theme = pd.DataFrame({'id': sets_per_theme.index, 'set_count': sets_per_theme})
print(type(sets_per_theme))
print(f"\n")
themes_df = pd.read_csv("data/themes.csv")

merged_df = pd.merge(sets_per_theme, themes_df, on="id")

print(merged_df)

# Graph out the top 10 from the merged dataframe
plt.figure(figsize=(14,10))
plt.xticks(fontsize=12, rotation=45)        # Rotate the X-Axis labels
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df["name"][:10], merged_df["set_count"][:10])
plt.show()