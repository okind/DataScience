

#Basic Pandas functions and data manipulation
import pandas as pd


# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("/Users/olga/Development/DataScience/Python/city_education_age_data.csv")
print(user_data.head(20))

# Categorize users by age
user_data.loc[user_data.age < 31, "age_status"] = "young"
user_data.loc[user_data.age >= 31, "age_status"] = "old"
print(user_data.head(20))

#Pandas main data types
#series 1-dimensional column
series = pd.Series(["BMW", "Toyota", "Honda"])
colours = pd.Series(["Red", "Blue", "White"])
odometer =  pd.Series(["9500", "2500", "500"])
#DataFrame - 2-dimensional
car_data = pd.DataFrame({"Car Make": series, "Colours": colours, "Odometer KM": odometer})
print(car_data)
car_data.to_csv("exported_car_data.csv")

#type of columns
print(car_data.dtypes)

#list of columns in DataFrame
print(car_data.columns)

#index column
print(car_data.index)

#statistical info about numerical columns
print(car_data.describe())

print(car_data.info())

#mean
print(odometer.mean())

#combines all columns in one
print(car_data.sum())

print(car_data["Odometer KM"].sum())

#loc - position, iloc - index, index can be different from position

print(car_data["Odometer KM"])
print(car_data.loc[1])

print(car_data.iloc[2])

#Car colours column
print(car_data.Colours)

#Filter for records
print(car_data[car_data["Car Make"] == "Toyota"])
