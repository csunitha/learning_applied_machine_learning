# Kaggle Intro to ML - Lesson 2

import pandas as pd 

# load the melbourne housing data
melbourne_file_path = "kaggle/input/day2_melbourne_housing_snapshot/melb_data.csv"
melbourne_data  = pd.read_csv(melbourne_file_path)

# listing all columns in data frame
print(melbourne_data.columns)

# the describe statement provides 8 values - count, mean, std, min, 25%, 50%, 75%, max
print(melbourne_data.describe())

# dropna drops missing values (think of na as 'not available')
melbourne_data = melbourne_data.dropna(axis=0)

# the describe statement provides 8 values - count, mean, std, min, 25%, 50%, 75%, max
print(melbourne_data.describe())

# selecting a prediction target using dot notation - here we will select price 
# by convention prediction target is called y 
y = melbourne_data.Price

# selecting the features - here we will select Rooms, Bathroom, Landsize, Lattitude, Longitude
# by convention this features data is called X
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

print(X.describe())
print(X.head())