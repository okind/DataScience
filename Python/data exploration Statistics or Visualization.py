#Exploring Data using Descriptive Statistics and Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs
user_data = pd.read_csv("city_education_age_data.csv")
pop_data = pd.read_csv("population_data.csv")
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Plot histogram
age = user_data["age"]
sns.displot(age)
plt.show()

# Mean age location
location_mean_age = new_df.groupby("location").age.mean()
print(location_mean_age)

# Plot barplot
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
    y= "age"
)
plt.show()

# Plot violinplot
plt.close()
sns.violinplot(x="location", y="age", data=new_df)
plt.show()
# Plot scatter plot
plt.close()
x = new_df["population_proper"]
y = new_df["age"]

plt.scatter(x, y, alpha=0.5)
plt.show()

# Plot linear regression:

sns.regplot(x="population_proper", y="age", data=new_df)
plt.show()
