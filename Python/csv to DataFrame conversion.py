
#Data cleaning with python framework Pandas
import pandas as pd


# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("city_education_age_data.csv")
print(user_data.head(20))

# Categorize users by age
user_data.loc[user_data.age < 31, "age_status"] = "young"
user_data.loc[user_data.age >= 31, "age_status"] = "old"
print(user_data.head(20))
