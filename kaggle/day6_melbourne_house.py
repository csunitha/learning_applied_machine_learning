import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#load housing data
filepath = "kaggle/input/melbourne_housing_snapshot/melb_data.csv"
housing_data = pd.read_csv(filepath)

#cleanup data
filtered_data = housing_data.dropna(axis=0)

#set target and prediction 
y = filtered_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_data[melbourne_features]

# split training and test data 
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# build model using RandomTreeRegressor
from sklearn.ensemble import RandomForestRegressor
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melbourne_prediction = forest_model.predict(val_X)
print("mean absolute error ", mean_absolute_error(val_y, melbourne_prediction)) 