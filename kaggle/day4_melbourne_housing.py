# Kaggle Intro to ML - Lesson 4 - Model Validation 

import pandas as pd 

# load the melbourne housing data
melbourne_file_path = "kaggle/input/melbourne_housing_snapshot/melb_data.csv"
melbourne_data  = pd.read_csv(melbourne_file_path)

# filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split
# split data into training and validation data, for both features and target
# the split is based on a random number generator. Supplying a numeric value to 
# the random_state argument guarantees we get the same split every time we 
# run this script
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

from sklearn.tree import DecisionTreeRegressor
# step 1: Define model
melbourne_model = DecisionTreeRegressor(random_state=1)
# step 2: Fit model with train data 
melbourne_model.fit(train_X, train_y)


# calculate MAE (Mean Absolute Error) on test data
from sklearn.metrics import mean_absolute_error
val_predictions = melbourne_model.predict(val_X.head())
print("\n\npredicted values ", val_predictions)
print(    "actual values    ", val_y.head().tolist())
print("MAE(mean absolute error) ", mean_absolute_error(val_y.head(), val_predictions), "\n\n")

