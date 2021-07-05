# Kaggle Intro to ML - Lesson 3

import pandas as pd 

# load the melbourne housing data
melbourne_file_path = "kaggle/input/melbourne_housing_snapshot/melb_data.csv"
melbourne_data  = pd.read_csv(melbourne_file_path)

# dropna drops missing values (think of na as 'not available')
melbourne_data = melbourne_data.dropna(axis=0)

# selecting a prediction target using dot notation - here we will select price 
# by convention prediction target is called y 
y = melbourne_data.Price

# selecting the features - here we will select Rooms, Bathroom, Landsize, Lattitude, Longitude
# by convention this features data is called X
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

print(X.describe())
print(X.head())

from sklearn.tree import DecisionTreeRegressor

# step 1: Define model
melbourne_model = DecisionTreeRegressor(random_state=1)

# step 2: Fit model
melbourne_model.fit(X, y)

# step 3: Predict
print("making predictions for the following 5 houses")
print(X.head())
print("predictions are ")
print(melbourne_model.predict(X.head()))

# step 4: Evaluate 