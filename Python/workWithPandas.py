import pandas
import requests
import csv
# make API request in Python
r = requests.get(
    'https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')
r_text = r.text
print(r_text)

r_json = r.json()

# convert json data to csv file
with open('commute_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(r.json())

# read csv to DataFrame object
commute_df = pandas.read_csv('commute_data.csv')

# rename columns
commute_df.columns = ['county', 'total_commuters',
                      'commutes', 'state id', 'county id']
print(commute_df.head())

#binomial destribution
#To use the random.binomial() method, we have to tell it how many trials we want to simulate (n) and the probability of ‘success’ in a single trial (p), and how many experiments to run
#100 toses, each element in the result set is number of successes in the experiment
import numpy
print(numpy.random.binomial(n = 100, p = 0.8, size = 500))

#flip coin simulation, result is a set of 0 and 1
print(numpy.random.binomial(n = 1, p = 0.5, size=200))
