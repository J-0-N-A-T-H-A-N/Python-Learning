import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")


clean_df = df.dropna()

max_starting = clean_df["Undergraduate Major"].loc[clean_df["Mid-Career Median Salary"].idxmax()]
print(f"\n{max_starting} has the highest Mid-Career Median Salary: ${clean_df['Mid-Career Median Salary'].max()}")

low_starting = clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmin()]
print(f"{low_starting} has the lowest Starting Salary: ${clean_df['Starting Median Salary'].min()}")

min_starting = clean_df["Undergraduate Major"].loc[clean_df["Mid-Career Median Salary"].idxmin()]
print(f"{min_starting} has the lowest Mid-Career Median Salary: ${clean_df['Mid-Career Median Salary'].min()}")


diff = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(6, "Spread", diff)


lowest_risk = clean_df["Undergraduate Major"].loc[clean_df["Spread"].idxmin()]
print(f"The Lowest Risk Major is {lowest_risk}")
print(clean_df.sort_values("Spread"))

# Majors with highest Potential
highest_potential = clean_df["Undergraduate Major"].loc[clean_df["Mid-Career 90th Percentile Salary"].idxmax()]
print(f"Highest Potential Major: {highest_potential} with a salary of {clean_df['Mid-Career 90th Percentile Salary'].max()}")

# Top 5
sorted_by_potential = clean_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
print(f"Top 5 highest potential:\n======================== \n{sorted_by_potential.head()}")

# Top 5 by Spread
top_spread = clean_df.sort_values(by="Spread", ascending=False)
print(f"Top 5 highest spread:\n==================== \n{top_spread.head()}")

