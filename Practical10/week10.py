# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the working directory to where the data file is located
os.chdir("/Users/pro/Desktop/IBI1_2024-25/Practical10")

# Check the current working directory and list files in it
print("Current working directory:", os.getcwd())
print("Files in the directory:", os.listdir())

# Read the CSV file into a DataFrame
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of the DataFrame:")
print(dalys_data.head(5))

# Get information about the DataFrame
print("\nDataFrame information:")
dalys_data.info()

# Get descriptive statistics for the DataFrame
print("\nDataFrame descriptive statistics:")
print(dalys_data.describe())

# Display the third column (Year) for the first 10 rows
first_10_years = dalys_data.iloc[0:10, 2]
print("\nThird column (Year) for the first 10 rows:")
print(first_10_years)

# Identify the 10th year with DALYs data recorded in Afghanistan
afghanistan_row = dalys_data[(dalys_data['Entity'] == 'Afghanistan')].iloc[9]
afghanistan_year = afghanistan_row['Year']
print("The 10th year with DALYs data recorded in Afghanistan:", afghanistan_year)

# Use a boolean to show DALYs for all countries in 1990
dalys_1990 = dalys_data.loc[dalys_data['Year'] == 1990, ['Entity', 'DALYs']]
print("\nDALYs for all countries in 1990:")
print(dalys_1990)
# Compare mean DALYs values for the UK and France
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
france_data = dalys_data[dalys_data['Entity'] == 'France']

uk_mean = uk_data['DALYs'].mean()
france_mean = france_data['DALYs'].mean()

print("\nMean DALYs in the UK:", uk_mean)
print("Mean DALYs in France:", france_mean)

if uk_mean > france_mean:
    print("The UK has a higher mean DALYs than France.")
else:
    print("France has a higher mean DALYs than the UK.")

# draw picture
plt.figure(figsize=(10, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b+')
plt.title('DALYs in the UK Over Time')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(rotation=-90)
plt.tight_layout()
plt.show()

# Question: How has the DALYs changed in China over time?
china_data = dalys_data[dalys_data['Entity'] == 'China']
plt.figure(figsize=(10, 6))
plt.plot(china_data['Year'], china_data['DALYs'], 'r-')
plt.title('DALYs in China Over Time')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(rotation=-90)
plt.tight_layout()
plt.show()