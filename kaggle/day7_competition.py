# Competition is to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 
# Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and 
# the logarithm of the observed sales price. 
# (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

import pandas as pd 
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# load data 
filepath = "kaggle/input/day7_competition_ames_housing_dataset/train.csv"
home_data = pd.read_csv(filepath)

# set target and prediction features 
y = home_data.SalePrice
features = ['LotArea',  'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'YrSold', 'GrLivArea', 'TotRmsAbvGrd', 'GarageCars']
X = home_data[features]

# split train and test data 
train_X, val_X, train_y, val_Y = train_test_split(X, y, random_state=1)

# measure root-mean-squared-error 
def get_rmse(X_val, y_val, max_leaf_nodes):
    rfr_model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    rfr_model.fit(X_val, y_val)
    training_predictions = rfr_model.predict(X_val)
    training_mse = mean_squared_error(y_val, training_predictions)
    training_rmse = math.sqrt(training_mse)
    return training_rmse

# try for different features / different leaf node
# for max_leaf_nodes in [5, 50, 500, 650, 5000]:
#     rmse = get_rmse(train_X, train_y, max_leaf_nodes)
#     print("SPLIT TRAINING DATA max leaf nodes is {} and rmse is {}".format(max_leaf_nodes, rmse))

scores = {leaf_node: get_rmse(train_X, train_y, leaf_node) for leaf_node in [5, 50, 500, 650]}
best_leaf_node = min(scores, key=scores.get)
print("\n\nBest tree size is : {}".format(best_leaf_node))

# with optimum feature / leaf node - run on full train data 
full_data_rmse = get_rmse(X, y, best_leaf_node)
print("\nFULL TRAINING DATA max leaf nodes is {} and rmse is {}".format(best_leaf_node, full_data_rmse))

# with optimum feature / leaf node - run on test data 
test_file_path = "kaggle/input/day7_competition_ames_housing_dataset/test.csv"
unfiltered_test_data = pd.read_csv(test_file_path)
test_data = unfiltered_test_data.dropna(axis=0)
model = RandomForestRegressor(max_leaf_nodes=best_leaf_node, random_state=1)
model.fit(X, y)
print(features)
test_X = test_data[features]
test_preds = model.predict(test_X)
output = pd.DataFrame({'Id': test_data.Id,'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)

# output = pd.DataFrame({'Id': test_data.Id,
#                        'SalePrice': test_preds})
# output.to_csv('submission.csv', index=False)


# prepare data file for submission