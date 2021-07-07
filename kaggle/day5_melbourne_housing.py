# Kaggle Intro to ML - Lesson 5 - Underfitting and overfitting 

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

# define method to measure MAE for different tree depth
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
def get_mae(max_leaf_nodes, train_X, test_X, train_y, test_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    prediction = model.predict(test_X)
    mae = mean_absolute_error(test_y, prediction)
    return mae

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("max leaf nodes is {} and mae is {}".format(max_leaf_nodes, my_mae))

